from django.urls import path
from default_dota_app.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token),

    path('attributes/', AttributesView.as_view()),

    path('heroes/', HeroesView.as_view()),
    path('heroes/<str:hero_name>/', HeroDetailsView.as_view()),

    path('guides/<str:hero_name>/', AddGuideView.as_view()),
]
