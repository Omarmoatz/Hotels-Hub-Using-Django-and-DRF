from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .models import Room, Hotel, Booking
from datetime import datetime
from zoneinfo import ZoneInfo
import pytz

# Helper function to retrieve room data and calculate price
def get_room_details(room_selection):
    rooms_list = []
    rooms_price = 0

    for item in room_selection.values():
        room_id = int(item["room_id"])
        room = get_object_or_404(Room, id=room_id)
        rooms_list.append(room)
        rooms_price += float(room.price)

    return rooms_list, rooms_price

# Helper function to calculate total cost based on room price and days
def calculate_total_cost(rooms_price, checkin, checkout):
    date_format = "%Y-%m-%d"
    timezone = ZoneInfo("UTC")
    checkin_date = datetime.strptime(checkin, date_format).replace(tzinfo=timezone)
    checkout_date = datetime.strptime(checkout, date_format).replace(tzinfo=timezone)
    
    total_days = (checkout_date - checkin_date).days
    total_cost = float(rooms_price * total_days)
    
    return total_cost, total_days

# Helper function to check room selection in session
def check_room_selection_in_session(session):
    if "room_selection_obj" in session and len(session["room_selection_obj"]) > 0:
        return session["room_selection_obj"]
    return None
