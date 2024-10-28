from datetime import datetime
from decimal import Decimal
from django.utils import timezone
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

import pytz
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required

from apps.users.tasks import send_email
from apps.booking.services import RoomSelectionManager
from apps.booking.models import Booking, Coupon, Hotel, Room, RoomType


def check_avilability(request, slug):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        checkin = request.POST.get("checkin", "")
        checkout = request.POST.get("checkout", "")
        adults = request.POST.get("adults", "")
        children = request.POST.get("children", "")
        room_type = request.POST.get("room_type", "")

        hotel = get_object_or_404(Hotel, slug=slug)
        room_type = get_object_or_404(RoomType, hotel=hotel, slug=room_type)

        main_url = reverse("hotel:room_type_detail", args=(slug, room_type.slug))
        url2 = f"&email={email}&checkin={checkin}&checkout={checkout}"
        rest_url = f"&adults={adults}&children={children}"
        url_with_params = f"{main_url}?name={name}{url2}{rest_url}"
        return HttpResponseRedirect(url_with_params)
    return messages.error(request, "something Happened")


# it take its data from jQuery, AJAX
def room_selection_view(request):
    data = request.GET
    room_selection = {}

    room_selection["room-selection" + str(data["room_id"])] = {
        "hotel_id": data["hotel_id"],
        "hotel_name": data["hotel_name"],
        "room_id": data["room_id"],
        "room_type": data["room_type"],
        "room_price": data["room_price"],
        "room_num": data["room_num"],
        "room_view": data["room_view"],
        "num_of_beds": data["num_of_beds"],
        "checkin": data["checkin"],
        "checkout": data["checkout"],
        "adults": data["adults"],
        "children": data["children"],
    }

    if "room_selection_obj" in request.session:
        current_id = data["room_id"]
        if current_id in request.session["room_selection_obj"]:
            old_data = request.session["room_selection_obj"]
            old_data[current_id]["adults"] = int(room_selection[current_id]["adults"])
            old_data[current_id]["children"] = int(
                room_selection[current_id]["children"],
            )
            request.session["room_selection_obj"] = old_data
        else:
            old_data = request.session["room_selection_obj"]
            old_data.update(room_selection)
            request.session["room_selection_obj"] = old_data
    else:
        request.session["room_selection_obj"] = room_selection

    json_data = {
        "data": request.session["room_selection_obj"],
        "name": "omar moataz",
        "rooms_len": len(request.session["room_selection_obj"]),
    }

    return JsonResponse(json_data)

@login_required
def selected_rooms(request):
    if "room_selection_obj" not in request.session or not request.session["room_selection_obj"]:
        messages.warning(request, "You don't have any booked rooms yet!")
        return redirect("/")

    manager = RoomSelectionManager(request.session["room_selection_obj"])
    rooms_list, rooms_price = manager.get_selected_rooms()
    hotel = manager.get_hotel()

    first_item = next(iter(request.session["room_selection_obj"].values()))
    checkin = first_item["checkin"]
    checkout = first_item["checkout"]
    total_days = manager.calculate_total_days(checkin, checkout)
    total_cost = manager.calculate_total_cost(rooms_price, checkin, checkout)

    context = {
        "user": request.user,
        "selected_rooms": request.session["room_selection_obj"],
        "hotel": hotel,
        "rooms_list": rooms_list,
        "checkin": checkin,
        "checkout": checkout,
        "total_days": total_days,
        "adults": first_item["adults"],
        "children": first_item["children"],
        "total_cost": round(total_cost, 2),
    }
    return render(request, "booking/rooms_selected.html", context)


# it take its data from jQuery, AJAX
def delete_room_from_session(request):
    room_id = f"room-selection{request.GET['room_id']}"
    if "room_selection_obj" in request.session:
        if room_id in request.session["room_selection_obj"]:
            del request.session["room_selection_obj"][room_id]
            request.session.modified = True

        if not request.session["room_selection_obj"]:
            return JsonResponse({"rooms_len": 0})

        manager = RoomSelectionManager(request.session["room_selection_obj"])
        rooms_list, rooms_price = manager.get_selected_rooms()
        hotel = manager.get_hotel()

        first_item = next(iter(request.session["room_selection_obj"].values()))
        checkin = first_item["checkin"]
        checkout = first_item["checkout"]
        total_days = manager.calculate_total_days(checkin, checkout)
        total_cost = manager.calculate_total_cost(rooms_price, checkin, checkout)

        rendered_data = render_to_string(
            "includes/rooms.html",
            {
                "selected_rooms": request.session["room_selection_obj"],
                "hotel": hotel,
                "user": request.user,
                "rooms_list": rooms_list,
                "checkin": checkin,
                "checkout": checkout,
                "total_days": total_days,
                "adults": first_item["adults"],
                "children": first_item["children"],
                "total_cost": round(total_cost, 2),
            },
        )
        return JsonResponse({
            "rendered_data": rendered_data,
            "rooms_len": len(request.session["room_selection_obj"]),
        })

    messages.warning(request, "You deleted all your booked rooms!")
    return redirect("/")


def checkout(request, booking_code):
    booking = get_object_or_404(Booking, booking_code=booking_code)
    return render(request, "booking/checkout.html", {"booking": booking})


@csrf_exempt
def create_booking(request):
    if "room_selection_obj" not in request.session or request.method != "POST":
        return redirect("/")

    manager = RoomSelectionManager(request.session["room_selection_obj"])
    rooms_list, rooms_price = manager.get_selected_rooms()
    hotel = manager.get_hotel()

    first_item = next(iter(request.session["room_selection_obj"].values()))
    checkin = first_item["checkin"]
    checkout = first_item["checkout"]
    total_days = manager.calculate_total_days(checkin, checkout)
    total_cost = manager.calculate_total_cost(rooms_price, checkin, checkout)

    booking = Booking.objects.create(
        user=request.user,
        full_name=request.POST["full_name"],
        phone=request.POST["phone"],
        email=request.POST["email"],
        hotel=hotel,
        total=total_cost,
        before_discount=total_cost,
        check_in_date=checkin,
        check_out_date=checkout,
        total_days=total_days,
        num_adults=first_item["adults"],
        num_children=first_item["children"],
        payment_method=Booking.PaymentStatus.Processing,
    )

    # Add rooms and room types to the booking
    for room in rooms_list:
        booking.room.add(room)
        booking.room_type.add(room.room_type)

    messages.success(request, "You booked successfully!")
    return redirect("booking:checkout", booking.booking_code)


# it take its data from jQuery, AJAX
@csrf_exempt
def check_coupun(request):
    if request.method == "POST":
        booking_id = request.POST["booking_id"]
        code = request.POST["coupon_code"]

        try:
            coupon = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Invalid coupon code."})

        booking = Booking.objects.get(id=booking_id)
        if booking.coupon == coupon:
            return JsonResponse(
                {"status": "error", "message": "you already used this coupon"},
            )

        if coupon and coupon.quantity > 0:
            today = datetime.now(tz=pytz.UTC).date()
            start_date = coupon.start.date()
            expire_date = coupon.end.date()

            if today >= start_date and today <= expire_date:
                discount_decimal = Decimal(coupon.discount) / 100
                discount = discount_decimal * booking.total
                booking.total -= discount

                booking.money_saved = discount
                booking.coupon = coupon
                coupon.quantity -= 1

                booking.save()
                coupon.save()

                html = render_to_string(
                    "includes/total_after_desount.html",
                    {"booking": booking},
                )
                return JsonResponse(
                    {
                        "status": "success",
                        "message": "Coupon applied successfully!",
                        "html": html,
                        "new_total": str(booking.total),
                    },
                )

            return JsonResponse({"status": "error", "message": "Expired coupon"})

        return JsonResponse({"status": "error", "message": "Cupon quntity is empty"})

    return JsonResponse({"status": "error", "message": "Invalid request method."})



def success_payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.payment_method = Booking.PaymentStatus.Paid
    booking.room.is_available = False
    booking.save()

    html_content = render_to_string("email/booking_confirmation.html", {"booking": booking})

    subject="Hotel Booking Confirmation",
    send_email.delay(subject, booking.email, html_content)

    if "room_selection_obj" in request.session:
        del request.session["room_selection_obj"]

    return render(request, "booking/success.html", {"booking": booking})


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    queryset = Booking.objects.all().order_by("-check_out_date")
    template_name = "booking/bookings_list.html"
    context_object_name = "bookings"

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return super().get_queryset()

        if user.user_type == user.UserType.USER:
            return super().get_queryset().filter(user=user)

        if user.user_type == user.UserType.SELLER:
            return super().get_queryset().filter(hotel__user=user)
        
        return super().get_queryset().none()

