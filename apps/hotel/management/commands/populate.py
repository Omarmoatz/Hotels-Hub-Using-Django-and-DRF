from random import choice
from random import randint

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

from apps.hotel.models import Hotel
from apps.hotel.models import HotelFeatures
from apps.hotel.models import HotelGallery
from apps.hotel.models import Review
from apps.hotel.models import Room
from apps.hotel.models import RoomType

fake = Faker()
User = get_user_model()


class Command(BaseCommand):
    help = "Populate the database with fake data"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int, help="Number of hotels to create")

    def handle(self, *args, **kwargs):
        n = kwargs["n"]

        # Create a user
        user, created = User.objects.get_or_create(username="testuser")
        if created:
            user.set_password("test@1234")
        user.email = "testuser@example.com"
        user.gender = "Male"
        user.phone = "1234567890"
        user.image = "profile/user.jpg"
        user.country = "United States"
        user.address = "123 Main St, City, State"
        user.facebook = "https://www.facebook.com/testuser"
        user.twitter = "https://www.twitter.com/testuser"
        user.save()

        # Create hotels
        for _ in range(n):
            hotel = Hotel(
                user=user,
                name=fake.company(),
                img=f"test/hotel{randint(1,12)}.jpeg",
                subtitle=fake.sentence(),
                description=fake.text(max_nb_chars=500),
                min_price=fake.random_number(digits=2),
                max_price=fake.random_number(digits=2),
                phone=fake.phone_number(),
                address=fake.address(),
                email=fake.email(),
                tag=choice(Hotel.TagChoices.choices)[0],
            )
            hotel.save()

            # Create hotel gallery images
            for _ in range(5):
                hotel_gallery = HotelGallery(
                    hotel=hotel,
                    img=f"test/hotel{randint(1,12)}.jpeg",
                )
                hotel_gallery.save()

            # Create hotel features
            for _ in range(4):
                selected_icon = choice(
                    [icon[0] for icon in HotelFeatures.IconFeatures.choices],
                )
                hotel_feature = HotelFeatures(
                    icon=selected_icon,
                    feature=selected_icon,
                )
                hotel_feature.save()
                hotel.feature.add(hotel_feature)

            # Create room types
            for _ in range(4):
                room_type = RoomType(
                    hotel=hotel,
                    title=fake.word(),
                    price_start=fake.random_number(digits=2),
                    price_end=fake.random_number(digits=2),
                    beds_num=fake.random_int(min=1, max=5),
                    room_size=fake.random_int(min=100, max=500),
                )
                room_type.save()

                # Create rooms  ''.join(choice(ascii_letters + digits) for _ in range(6))
                for _ in range(10):
                    room = Room(
                        hotel=hotel,
                        room_type=room_type,
                        room_num=randint(1, 100),
                        view=fake.word(),
                        price=fake.random_number(digits=2),
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

        self.stdout.write(self.style.SUCCESS(f"{n} hotels populated successfully!"))


# Running Command: python manage.py populate 10
