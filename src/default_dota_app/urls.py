from django.urls import path
from default_dota_app import views

urlpatterns = [
    path('heroes/', views.get_heroes, name='get_heroes'),
    path('heroes/<str:hero_name>', views.get_hero, name='get_hero'),
    path('stages/', views.get_stages),
    # path('heroes/<str:hero_name>/guides', views.get_guides, name='get_guides'),
]
