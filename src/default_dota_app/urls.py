from django.urls import path
from default_dota_app import views

urlpatterns = [
    path('', views.index, name='index'),
]