from django.urls import path, include

from default_dota_app.views import *

urlpatterns = [
    path('', documentation_links_view),

    path('attributes/', AttributesView.as_view()),

    path('heroes/', HeroesView.as_view()),
    path('heroes/<str:hero_name>/', HeroDetailsView.as_view()),

    path('guides/<str:id>/', GuideDetailsView.as_view()),
    path('guides/<str:hero_name>/create/', CreateGuideView.as_view()),

    path('items/', ItemsView.as_view()),
    path('items/<str:id>/', ItemsView.as_view()),

    # External urls
    path('auth/', include('default_dota_app.urls.auth_urls')),
    path('', include('default_dota_app.urls.swagger_urls')),
    path('', include('default_dota_app.urls.user_urls'))
]
