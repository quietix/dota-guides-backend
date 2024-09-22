from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include('default_dota_app.urls')),
    path('api/', include('default_dota_app.schema')),
]