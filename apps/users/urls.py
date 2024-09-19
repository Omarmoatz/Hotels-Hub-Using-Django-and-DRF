from django.urls import path

from .views import user_detail_view
from .views import user_redirect_view
from .views import user_update_view
from apps.users.views import sign_up, activate, login_view, logout_view

app_name = "users"
urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('activate/<str:username>', activate, name='activate'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
