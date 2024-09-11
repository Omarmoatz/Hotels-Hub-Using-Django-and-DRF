from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import sign_up, activate, login_view, logout_view
from accounts.api.views import UserViewSetApi

router = DefaultRouter()
router.register(r'api', UserViewSetApi)


app_name = 'accounts'

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('activate/<str:username>', activate, name='activate'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
] + router.urls
