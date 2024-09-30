from django.urls import path
from default_dota_app.views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-all-current-user-sessions/', LogoutAllCurrentUserSessionsView.as_view(), name='logout_all_current_sessions'),
    path('logout-all-users/', LogoutAllUsersView.as_view(), name='logout_all_users'),
]