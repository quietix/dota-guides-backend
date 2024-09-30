from django.urls import path
from default_dota_app.views.user_views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('users/', GetAllUsersView.as_view(), name='get_all_users'),
    path('user/<str:id>/', UserView.as_view(), name='get_user'),
]