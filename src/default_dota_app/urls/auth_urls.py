from django.urls import path
from default_dota_app.views.auth_views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout-all-current-user-sessions/', LogoutAllCurrentUserSessionsView.as_view(), name='logout_all_current_sessions'),
    path('logout-all-users/', LogoutAllUsersView.as_view(), name='logout_all_users'),
]