from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from default_dota_app.serializers.hero_serializers import ReadHeroPreviewSerializer, UpsertHeroSerializer
from default_dota_app.services import HeroService
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging

logger = logging.getLogger(__name__)

class HeroListView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @swagger_auto_schema(
        tags=["Heroes"],
        operation_summary="Retrieve All Heroes",
        operation_description="Get a list of all heroes along with their skills. Optionally filter heroes by name.",
        manual_parameters=[
            openapi.Parameter(
                'hero_name',
                openapi.IN_QUERY,
                description="Filter heroes by their name (hero_name contains input)",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'attribute_name',
                openapi.IN_QUERY,
                description="Filter heroes by attribute (attribute_name contains input)",
                type=openapi.TYPE_STRING
            )
        ],
        responses={
            200: openapi.Response('Successful retrieval of heroes', ReadHeroPreviewSerializer(many=True)),
        }
    )
    def get(self, request):
        hero_list_data = HeroService.get_hero_list(request)
        if hero_list_data:
            return Response(hero_list_data)
        return Response({"detail": "Failed to retrieve heroes."}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["Heroes"],
        operation_summary="Create a New Hero",
        operation_description="Create a new hero. Only accessible to admin users.",
        request_body=UpsertHeroSerializer,
        responses={
            201: openapi.Response('Hero created successfully', ReadHeroPreviewSerializer),
            403: 'Forbidden (user is not an admin)',
            400: openapi.Response(description='Invalid input data'),
        }
    )

    def post(self, request):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        created_hero = HeroService.create_hero(request)

        if created_hero:
            return Response(created_hero, status=status.HTTP_200_OK)
        return Response({"detail": "Create hero failed."}, status=status.HTTP_400_BAD_REQUEST)
