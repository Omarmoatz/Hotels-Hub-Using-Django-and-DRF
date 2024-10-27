from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from apps.booking.api.views import BookingViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
router.register("booking", BookingViewSet)

urlpatterns = router.urls

app_name = "booking"
