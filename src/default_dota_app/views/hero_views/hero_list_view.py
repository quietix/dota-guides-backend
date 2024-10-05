from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from default_dota_app.models import *
from default_dota_app.serializers.hero_serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging


logger = logging.getLogger(__name__)

class HeroListView(APIView):
    @swagger_auto_schema(
        tags=["Heroes"],
        operation_summary="Retrieve All Heroes",
        operation_description="Get a list of all heroes along with their skills. Optionally filter heroes by name.",
        manual_parameters=[
            openapi.Parameter(
                'hero_name',
                openapi.IN_QUERY,
                description="Filter heroes by their name",
                type=openapi.TYPE_STRING
            )
        ],
        responses={
            200: openapi.Response('Successful retrieval of heroes', ReadHeroPreviewSerializer(many=True)),
        }
    )
    def get(self, request):
        hero_name = request.GET.get('hero_name', None)

        if hero_name:
            heroes = Hero.objects.filter(hero_name__icontains=hero_name).prefetch_related('skills')
        else:
            heroes = Hero.objects.all().prefetch_related('skills')

        serializer = ReadHeroPreviewSerializer(heroes, many=True)
        return Response(serializer.data)

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

        serializer = UpsertHeroSerializer(data=request.data)
        if serializer.is_valid():
            hero = serializer.save()
            logger.info(f"User {request.user} created hero #{hero.id}.")
            return Response(ReadHeroPreviewSerializer(hero).data, status=status.HTTP_201_CREATED)

        logger.error(f"Failed to create hero. User: {request.user}, Errors: {serializer.errors}.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
