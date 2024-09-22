from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from default_dota_app import views

schema_view = get_schema_view(
    openapi.Info(
        title="Dota Guides API",
        default_version='v1',
        description="API documentation for Dota Guides",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Main API paths
    path('heroes/', views.get_heroes, name='get_heroes'),
    path('heroes/<str:hero_name>/', views.get_hero_details, name='get_hero_details'),
    path('heroes/<str:hero_name>/guides/', views.get_hero_guides, name='get_hero_guides'),
    path('guides/<str:guide_id>/', views.get_guide_details, name='get_guide_details'),
    path('attributes/', views.get_attributes, name='get_attributes'),

    # Test API paths
    path('items/', views.get_items, name='get_items'),
    path('stages/', views.get_stages, name='get_stages'),
    path('guides/', views.get_guides, name='get_guides'),
    path('skills/', views.get_skills, name='get_skills'),
    path('item-wrappers/', views.get_item_wrappers, name='get_item_wrappers'),
]
