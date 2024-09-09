from django.contrib.auth import get_user_model
from django.core.files import File
from django.utils.text import slugify
from random import choice
from string import ascii_letters, digits
from faker import Faker
from hotel.models import Hotel, HotelGallery, HotelFeatures, RoomType, Room, Review

fake = Faker()
User = get_user_model()

def populate_data():
    # Create a user
    user = User.objects.create_user(username='testuser', password='testpassword')

    # Create hotels
    for _ in range(10):
        hotel = Hotel(
            user=user,
            name=fake.company(),
            img=File(open('path/to/image.jpg', 'rb')),
            subtitle=fake.sentence(),
            description=fake.paragraph(),
            min_price=fake.random_number(digits=4),
            max_price=fake.random_number(digits=4),
            phone=fake.phone_number(),
            address=fake.address(),
            email=fake.email(),
            tag=choice([tag[0] for tag in Hotel.TAG_CHOICES]),
        )
        hotel.save()

        # Create hotel gallery images
        for _ in range(5):
            hotel_gallery = HotelGallery(
                hotel=hotel,
                img=File(open('path/to/image.jpg', 'rb')),
            )
            hotel_gallery.save()

        # Create hotel features
        for _ in range(3):
            hotel_feature = HotelFeatures(
                icon=choice([icon[0] for icon in HotelFeatures.ICON_FEATURES]),
                feature=fake.word(),
            )
            hotel_feature.save()
            hotel.feature.add(hotel_feature)

        # Create room types
        for _ in range(5):
            room_type = RoomType(
                hotel=hotel,
                title=fake.word(),
                price_start=fake.random_number(digits=4),
                price_end=fake.random_number(digits=4),
                beds_num=fake.random_int(min=1, max=5),
                room_size=fake.random_int(min=10, max=50),
            )
            room_type.save()

            # Create rooms
            for _ in range(10):
                room = Room(
                    hotel=hotel,
                    room_type=room_type,
                    room_num=''.join(choice(ascii_letters + digits) for _ in range(6)),
                    view=fake.word(),
                    price=fake.random_number(digits=4),
                    is_available=fake.boolean(),
                )
                room.save()

        # Create reviews
        for _ in range(5):
            review = Review(
                hotel=hotel,
                user=user,
                content=fake.paragraph(),
                rate=choice([rate[0] for rate in Review.RATE.choices]),
            )
            review.save()

populate_data()