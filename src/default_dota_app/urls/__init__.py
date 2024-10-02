from django.urls import path, include

from default_dota_app.views import *

urlpatterns = [
    path('', documentation_links_view, name='documentation'),
    path('', include('default_dota_app.urls.user_urls')),
    path('', include('default_dota_app.urls.urls')),
    path('', include('default_dota_app.urls.swagger_urls')),
    path('auth/', include('default_dota_app.urls.auth_urls')),
]
