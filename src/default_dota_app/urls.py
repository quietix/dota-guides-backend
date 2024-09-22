from django.urls import path
from default_dota_app import views

urlpatterns = [
    path('heroes/', views.get_heroes, name='get_heroes'),
    path('heroes/<str:hero_name>/', views.get_hero_details, name='get_hero_details'),
    path('heroes/<str:hero_name>/guides/', views.get_hero_guides, name='get_hero_guides'),
    path('heroes/<str:hero_name>/skills/', views.get_skills, name='get_skills'),
    path('guides/<str:guide_id>/', views.get_guide_details, name='get_guide_details'),
    path('attributes/', views.get_attributes, name='get_attributes'),
]
