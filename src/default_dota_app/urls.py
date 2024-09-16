from django.urls import path
from default_dota_app import views

urlpatterns = [
    path('heroes/', views.get_heroes, name='get_heroes'),
    path('heroes/<str:hero_name>', views.get_hero, name='get_hero'),
    path('items/', views.get_items, name='get_items'), # test
    path('item-wrappers/', views.get_item_wrappers, name='get_item_wrappers'),
    path('stages/', views.get_stages, name='get_stages'), # test
    path('guides/', views.get_guides, name='get_guides'), # test
    path('heroes/<str:hero_name>/guides/', views.get_hero_guides, name='get_hero_guides'),
]
