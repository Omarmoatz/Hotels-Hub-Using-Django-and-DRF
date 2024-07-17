from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Booking,Hotel,Room,RoomType


def check_avilability(request,slug):
    if request.method == 'POST': 
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        checkin = request.POST.get('checkin','')
        checkout = request.POST.get('checkout','')
        adults = request.POST.get('adults','')
        children = request.POST.get('children','')
        room_type = request.POST.get('room_type','')

        hotel = get_object_or_404(Hotel,slug=slug)
        room_type = get_object_or_404(RoomType, hotel=hotel, slug=room_type)
        
        url = reverse('hotel:room_type_detail', args=(slug, room_type.slug))
        url_with_params = f'{url}?id={hotel.id}&name={name}&email={email}&checkin={checkin}&checkout={checkout}&adults={adults}&children={children}&room_type={room_type}'
        return HttpResponseRedirect(url_with_params)



def room_selection_view(request):
    data = request.GET
    room_selection = {}

    room_selection[str(data['id'])] = {
        'hotel_id' : data['hotel_id'],
        'hotel_name' : data['hotel_name'],
        'room_id' : data['room_id'],
        'room_type' : data['room_type'],
        'room_price' : data['room_price'],
        'room_num' : data['room_num'],
        'room_view' : data['room_view'],
        'num_of_beds' : data['num_of_beds'],
        'checkin' : data['checkin'],
        'checkout' : data['checkout'],
        'adults' : data['adults'],
        'children' : data['children'],
    }

    room_selection_session = request.session['room_selection_obj']
    if 'room_selection_obj' in request.session:
        current_id = data['id']
        if current_id in room_selection_session:
            old_data = room_selection_session
            old_data[current_id]['adults'] = int(room_selection[current_id]['adults'])
            old_data[current_id]['children'] = int(room_selection[current_id]['children'])
            room_selection_session = old_data
        else:
            old_data = room_selection_session
            old_data.update(room_selection)
            room_selection_session = old_data

    else:
        room_selection_session = room_selection

    json_data = {
        'data': room_selection_session,
        'name' : 'omar moataz',
        'data_count' : room_selection_session
    }

    return JsonResponse(json_data)



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
