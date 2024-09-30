from django.urls import path
from default_dota_app.views.user_views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    # path('read-all-users/', ReadAllUsersView.as_view(), name='read_all_users'),
]