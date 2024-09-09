import os ,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth import get_user_model
from hotel.models import Hotel, HotelGallery, HotelFeatures, RoomType, Room, Review

User = get_user_model()

def delete_test_data():
    User.objects.filter(username='testuser').delete()
    Hotel.objects.filter(user__username='testuser').delete()
    print('Test data deleted successfully!')

delete_test_data()
# print(HotelFeatures.ICON_FEATURES[selected_icon],)