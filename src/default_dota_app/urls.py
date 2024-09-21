from django.urls import path
from default_dota_app import views

urlpatterns = [
    path('heroes/', views.get_heroes, name='get_heroes'),
    path('heroes/<str:hero_name>', views.get_hero, name='get_hero'),
    path('item-wrappers/', views.get_item_wrappers, name='get_item_wrappers'),
    path('heroes/<str:hero_name>/guides/', views.get_hero_guides, name='get_hero_guides'),
    path('attributes/', views.get_attributes, name='get_attributes'),

    # Test
    path('items/', views.get_items, name='get_items'),
    path('stages/', views.get_stages, name='get_stages'),
    path('guides/', views.get_guides, name='get_guides'),
]
