from django.test import TestCase
from apps.users.models import User
from hotel.models import Hotel

class HotelTestCase(TestCase):
    def test_hotel_property(self):
        user = User(username='testuser')
        user.save()
        hotel = Hotel(user=user, name='Hotel Test', address='Test Address', phone='1234567890')
        hotel.save()  
        self.assertEqual(hotel.check_created_at_this_year, True)

        hotel.address = 'Test Address 2'
        self.assertEqual(hotel.address, 'Test Address')
