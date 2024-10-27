
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from apps.hotel.api.views import HotelApiView, RoomTypeApiView

router = DefaultRouter() if settings.DEBUG else SimpleRouter()


router = DefaultRouter()
router.register("hotel", HotelApiView, basename="hotel")
router.register(
    r"hotel/(?P<hotel_pk>\d+)/room-type",
    RoomTypeApiView,
    basename="roomtype",
)

urlpatterns = router.urls

app_name = "api"
