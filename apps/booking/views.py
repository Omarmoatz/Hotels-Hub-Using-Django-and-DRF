from datetime import datetime
from decimal import Decimal
from zoneinfo import ZoneInfo

import pytz
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from .models import Booking
from .models import Coupon
from .models import Hotel
from .models import Room
from .models import RoomType


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

        url = reverse("hotel:room_type_detail", args=(slug, room_type.slug))
        url2 = f"&email={email}&checkin={checkin}&checkout={checkout}"
        rest_url = f"&adults={adults}&children={children}&room_type={room_type}"
        url_with_params = f"{url}?hotel_id={hotel.id}&name={name}{url2}{rest_url}"
        return HttpResponseRedirect(url_with_params)
    return messages.error(request, "something Happened")


# it tooks its data from jQuery, AJAX
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


def selected_rooms(request):
    rooms_price = 0
    rooms_list = []
    if "room_selection_obj" in request.session:
        if len(request.session["room_selection_obj"]) == 0:
            messages.warning(request, "You deleted all your booked rooms!")
            return redirect("/")

        for item in request.session["room_selection_obj"].values():
            hotel_id = int(item["hotel_id"])
            room_id = int(item["room_id"])
            checkin = item["checkin"]
            checkout = item["checkout"]
            adults = int(item["adults"])
            children = int(item["children"])

            room = get_object_or_404(Room, id=room_id)
            rooms_list.append(room)
            rooms_price += float(room.price)

        hotel = Hotel.objects.get(id=hotel_id)

        date_format = "%Y-%m-%d"
        timezone = ZoneInfo(
            "UTC",
        )

        checkin_date = datetime.strptime(checkin, date_format).replace(tzinfo=timezone)
        checkout_date = datetime.strptime(checkout, date_format).replace(
            tzinfo=timezone,
        )
        total_days = (checkout_date - checkin_date).days

        total_cost = float(rooms_price * total_days)

        context = {
            "selected_rooms": request.session["room_selection_obj"],
            "hotel": hotel,
            "rooms_list": rooms_list,
            "checkin": checkin,
            "checkout": checkout,
            "total_days": total_days,
            "adults": adults,
            "children": children,
            "total_cost": round(total_cost, 2),
        }

        return render(request, "hotel/rooms_selected.html", context)

    messages.warning(request, "You Dont Have Any Booked Rooms Yet!")
    return redirect("/")


# it tooks its data from jQuery, AJAX
def delete_room_from_session(request):
    room_id = "room-selection" + str(request.GET["room_id"])
    rooms_price = 0
    rooms_list = []
    if "room_selection_obj" in request.session:
        if room_id in request.session["room_selection_obj"]:
            existing_data = request.session["room_selection_obj"]
            del request.session["room_selection_obj"][room_id]
            request.session["room_selection_obj"] = existing_data

        if len(request.session["room_selection_obj"]) == 0:
            return JsonResponse(
                {"rooms_len": len(request.session["room_selection_obj"])},
            )

        for item in request.session["room_selection_obj"].values():
            hotel_id = int(item["hotel_id"])
            room_id = int(item["room_id"])
            checkin = item["checkin"]
            checkout = item["checkout"]
            adults = int(item["adults"])
            children = int(item["children"])

            room = Room.objects.get(id=room_id)
            rooms_list.append(room)
            rooms_price += float(room.price)

        hotel = Hotel.objects.get(id=hotel_id)

        date_format = "%Y-%m-%d"
        timezone = pytz.UTC
        checkin_date = datetime.strptime(checkin, date_format).replace(tzinfo=timezone)
        checkout_date = datetime.strptime(checkout, date_format).replace(
            tzinfo=timezone,
        )

        # Calculate total days
        total_days = (checkout_date - checkin_date).days

        total_cost = float(rooms_price * total_days)

        rendered_data = render_to_string(
            "includes/rooms.html",
            {
                "selected_rooms": request.session["room_selection_obj"],
                "hotel": hotel,
                "rooms_list": rooms_list,
                "checkin": checkin,
                "checkout": checkout,
                "total_days": total_days,
                "adults": adults,
                "children": children,
                "total_cost": round(total_cost, 2),
            },
        )
        return JsonResponse(
            {
                "rendered_data": rendered_data,
                "rooms_len": len(request.session["room_selection_obj"]),
            },
        )

    messages.warning(request, "You deleted all your booked rooms!")
    return redirect("/")


def checkout(request, booking_code):
    booking = Booking.objects.get(booking_code=booking_code)
    return render(request, "booking/checkout.html", {"booking": booking})


@csrf_exempt
def create_booking(request):
    total_rooms_price = 0
    rooms_obj = []
    if "room_selection_obj" in request.session:
        if request.method == "POST":
            for item in request.session["room_selection_obj"].values():
                hotel_id = item["hotel_id"]
                room_id = item["room_id"]
                checkin = item["checkin"]
                checkout = item["checkout"]
                adults = item["adults"]
                children = item["children"]

                room = Room.objects.get(id=room_id)
                total_rooms_price += room.price
                rooms_obj.append(room)

            hotel = Hotel.objects.get(id=hotel_id)

            date_format = "%Y-%m-%d"
            checkin_date = datetime.strptime(checkin, date_format).replace(
                tzinfo=pytz.UTC,
            )
            checkout_date = datetime.strptime(checkout, date_format).replace(
                tzinfo=pytz.UTC,
            )
            total_days = (checkout_date - checkin_date).days

            total_price = total_rooms_price * total_days
            user = request.user

            full_name = request.POST["full_name"]
            email = request.POST["email"]
            phone = request.POST["phone"]

            booking = Booking.objects.create(
                user=user,
                full_name=full_name,
                phone=phone,
                email=email,
                hotel=hotel,
                total=total_price,
                before_discount=total_price,
                check_in_date=checkin,
                check_out_date=checkout,
                total_days=total_days,
                num_adults=adults,
                num_children=children,
                payment_method= Booking.PaymentStatus.Proccing,
            )

            for item in rooms_obj:
                room_type = item.room_type

                booking.room.add(item)
                booking.room_type.add(room_type)

            messages.success(request, "You Booked Sucesfully")
    return redirect("booking:checkout", booking.booking_code)


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
                    },
                )

            return JsonResponse({"status": "error", "message": "Expired coupon"})

        return JsonResponse({"status": "error", "message": "Cupon quntity is empty"})

    return JsonResponse({"status": "error", "message": "Invalid request method."})



def success_payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)

    # Update the booking details
    booking.payment_method = Booking.PaymentStatus.Paid
    booking.room.is_available = True
    booking.save()

    html_content = render_to_string("email/booking_confirmation.html", {"booking": booking})
    text_content = strip_tags(html_content)  # Create a plain-text version by stripping HTML tags

    # Sending the email
    email = EmailMultiAlternatives(
        subject="Hotel Booking Confirmation",
        body=text_content,  # Fallback plain-text body
        from_email=booking.hotel.email,
        to=[booking.email]
    )
    email.attach_alternative(html_content, "text/html")  # Attach the HTML version
    email.send()

    if "room_selection_obj" in request.session:
        del request.session["room_selection_obj"]

    return render(request, "booking/success.html", {"booking": booking})



# class CheckAvilability(generic.CreateView):
#     model = Booking
#     form_class = BokingForm
#     template_name = 'hotel/check_availability.html'
#     success_url = 'hotel/'

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context["room_type"] = models.RoomType.objects.filter(hotel =self.get_object())
#     #     return context


#     def form_valid(self, form):
#         slug = self.kwargs['slug']
#         room_type = self.kwargs['room_type']
#         user = self.request.user

#         hotel = get_object_or_404(Hotel, slug=slug)
#         # room_type = models.RoomType.objects.filter(hotel=hotel)
#         room = Room.objects.filter(hotel=hotel, room_type=room_type)

#         print( hotel, room, room_type,'-------------------')

#         form.instance.hotel = hotel
#         form.instance.room = room
#         form.instance.room_type = room_type


#         if user.is_authenticated:
#             form.instance.user = user

#         # self.success_url = f'/hotels/{slug}/ckeck_avilability/'
#         return super().form_valid(form)
