
import pytz
from datetime import datetime
from django.shortcuts import get_object_or_404

from apps.hotel.models import Room, Hotel

class RoomSelectionManager:
    def __init__(self, session_data):
        self.session_data = session_data

    def get_selected_rooms(self):
        rooms = []
        total_price = 0
        for item in self.session_data.values():
            room = get_object_or_404(Room, id=int(item["room_id"]))
            rooms.append(room)
            total_price += room.price
        return rooms, total_price

    def get_hotel(self):
        if self.session_data:
            hotel_id = int(next(iter(self.session_data.values()))["hotel_id"])
            return get_object_or_404(Hotel, id=hotel_id)
        return None

    @staticmethod
    def calculate_total_days(checkin, checkout):
        date_format = "%Y-%m-%d"
        checkin_date = datetime.strptime(checkin, date_format).replace(tzinfo=pytz.UTC)
        checkout_date = datetime.strptime(checkout, date_format).replace(tzinfo=pytz.UTC)
        return (checkout_date - checkin_date).days

    def calculate_total_cost(self, room_price, checkin, checkout):
        total_days = self.calculate_total_days(checkin, checkout)
        return room_price * total_days
