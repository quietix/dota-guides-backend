from django.urls import path
from default_dota_app.views.user_views import *

urlpatterns = [
    path('users/', GetAllUsersView.as_view(), name='get_all_users'),
    path('user/<str:id>/', UserView.as_view(), name='manage_user'),
    path('profile/', ProfileView.as_view(), name='profile'),
]