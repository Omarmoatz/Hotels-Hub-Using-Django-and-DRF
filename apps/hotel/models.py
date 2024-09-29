from django.db import models
from django.db.models.aggregates import Avg
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from apps.users.models import User


class Hotel(TimeStampedModel):
    class TagChoices(models.TextChoices):
        SALE = "sale", _("Sale")
        NEW = "new", _("New")
        FEATURED = "featured", _("Featured")
        CHEAP = "cheap", _("Cheap")
        LUXURY = "luxury", _("Luxury")
        POPULAR = "popular", _("Popular")

    user = models.ForeignKey(User, related_name="user_hotel", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="", blank=True)
    img = models.ImageField(upload_to="hotel/")
    subtitle = models.TextField(max_length=400, blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    min_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    max_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    phone = models.CharField(max_length=500, default="", blank=True)
    address = models.CharField(max_length=500, default="", blank=True)
    email = models.EmailField(max_length=500, default="", blank=True, null=True)
    feature = models.ManyToManyField("HotelFeatures")
    tag = models.CharField(
        max_length=500,
        default="",
        choices=TagChoices.choices,
        blank=True,
    )
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("hotel:hotel_detail", kwargs={"slug": self.slug})

    def get_api_url(self):
        localhost = "http://127.0.0.1:8000"
        return f"{localhost}{reverse('hotel:hotel-detail', kwargs={'slug': self.slug})}"

    @property
    def avg_rating(self):
        avg = self.hotel_review.aggregate(avg_rate=Avg("rate"))
        if not avg["avg_rate"]:
            return 0
        return round(avg["avg_rate"], 1)

    @property
    def check_created_at_this_year(self) -> bool:
        return self.created_at.year == timezone.now().year

    class Meta:
        ordering = ["-created"]


class HotelGallery(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        related_name="hotel_gallery",
        on_delete=models.CASCADE,
    )
    img = models.ImageField(upload_to="hotel gallery/")

    def __str__(self):
        return str(self.hotel)


class HotelFeatures(models.Model):
    class IconFeatures(models.TextChoices):
        BED = "bed", _("Bed")
        BATH = "bath", _("Bath")
        WIFI = "wifi", _("WiFi")
        TV = "tv", _("TV")
        FAN = "fan", _("Fan")
        LAUNDRY = "user-cog", _("Laundry")
        DINNER = "utensils", _("Dinner")

    icon = models.CharField(
        max_length=100,
        choices=IconFeatures.choices,
        blank=True,
    )
    feature = models.CharField(max_length=500, default="", blank=True)

    def __str__(self):
        return self.feature


class RoomType(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        related_name="hotel_room_type",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=500, default="", blank=True, null=True)
    price_start = models.DecimalField(max_digits=7, decimal_places=2)
    price_end = models.DecimalField(max_digits=7, decimal_places=2)
    beds_num = models.PositiveIntegerField()
    room_size = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Room(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        related_name="hotel_room",
        on_delete=models.CASCADE,
    )
    room_type = models.ForeignKey(
        RoomType,
        related_name="room_type",
        on_delete=models.CASCADE,
    )
    room_num = models.PositiveIntegerField()
    view = models.CharField(max_length=500, default="", blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return str(self.room_type)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.room_num)
        super().save(*args, **kwargs)

    def beds_num(self):
        return self.room_type.beds_num

    def room_size(self):
        return self.room_type.room_size


class Review(models.Model):
    class RATE(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    hotel = models.ForeignKey(
        Hotel,
        related_name="hotel_review",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, related_name="user_review", on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, blank=True, null=True)
    rate = models.CharField(max_length=50, choices=RATE.choices, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review {self.id} by {self.user!s} on {self.hotel}"
