from django.test import TestCase
from apps.hotel.models import Hotel

from apps.users.models import User


# class HotelTestCase(TestCase):
#     def test_hotel_property(self):
#         user = User(username="testuser")
#         user.save()
#         hotel = Hotel(
#             user=user,
#             name="Hotel Test",
#             address="Test Address",
#             phone="1234567890",
#         )
#         hotel.save()
#         assert not hotel.check_creation_date

#         hotel.address = "Test Address 2"
#         assert hotel.address == "Test Address"
