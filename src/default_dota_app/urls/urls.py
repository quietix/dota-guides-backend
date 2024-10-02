from django.urls import path
from default_dota_app.views import *

urlpatterns = [
    path('attributes/', AttributesView.as_view(), name='attributes_list'),

    path('heroes/', HeroesView.as_view(), name='heroes_list'),
    path('heroes/<str:hero_name>/', HeroDetailsView.as_view(), name='hero_crud'),

    path('guides/<str:id>/', GuideDetailsView.as_view(), name='guide_details'),
    path('guides/<str:hero_name>/create/', CreateGuideView.as_view(), name='create_guide'),

    path('item-sections/', ItemSectionListView.as_view(), name='item_section_list'),
    path('item-sections/<str:id>/', ItemSectionDetailsView.as_view(), name='item_section_details'),

    path('items/', ItemsListView.as_view(), name='items_list'),
    path('items/<str:id>/', ItemDetailsView.as_view(), name='item_details'),
]
