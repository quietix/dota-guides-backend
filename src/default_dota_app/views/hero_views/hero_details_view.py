from django.contrib.auth.models import User
from django.db.models import Prefetch
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from default_dota_app.models import *
from default_dota_app.serializers.hero_serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging

logger = logging.getLogger(__name__)

class HeroDetailsView(APIView):
    @swagger_auto_schema(
        tags=["Heroes"],
        operation_summary="Retrieve Hero Details",
        operation_description="Get detailed information about a hero by ID.",
        responses={
            200: openapi.Response('Successful retrieval of hero details', ReadHeroDetailsSerializer),
            404: openapi.Response(description='Hero not found.'),
        }
    )
    def get(self, request, id):
        if request.user.is_authenticated:
            user_guides = Guide.objects.filter(user=request.user)
        else:
            admin_user = User.objects.filter(is_superuser=True).first()
            user_guides = Guide.objects.filter(user=admin_user)

        prefetch_user_guides = Prefetch('guides', queryset=user_guides)
        hero = Hero.objects.filter(id=id).prefetch_related('skills', prefetch_user_guides).first()

        if not hero:
            logger.error(f"Hero #{id} not found for retrieval.")
            return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReadHeroDetailsSerializer(hero)
        logger.info(f"Retrieved details for hero #{id}.")
        return Response(serializer.data)

    @swagger_auto_schema(
        tags=["Heroes"],
        operation_summary="Update Hero Details",
        operation_description="Update an existing hero's details, including the image and attribute.",
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_PATH, description="ID of the hero to update", type=openapi.TYPE_INTEGER)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'hero_name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the hero'),
                'img': openapi.Schema(type=openapi.TYPE_FILE, description='Image of the hero (multipart/form-data)'),
                'attribute': openapi.Schema(type=openapi.TYPE_STRING, description='Attribute name (slug) for the hero'),
            },
        ),
        responses={
            200: openapi.Response('Hero updated successfully', ReadHeroDetailsSerializer),
            400: openapi.Response(description='Invalid input data.'),
            403: openapi.Response(description='User does not have permission to update the hero.'),
            404: openapi.Response(description='Hero not found.'),
        }
    )
    def patch(self, request, id):
        self.authentication_classes = [IsAdminUser]
        self.check_permissions(request)

        try:
            hero = Hero.objects.get(id=id)
            serializer = UpsertHeroSerializer(hero, data=request.data, partial=True)

            if serializer.is_valid():
                hero = serializer.save()
                logger.info(f"User {request.user} updated details for hero #{id}.")
                return Response(ReadHeroPreviewSerializer(hero).data, status=status.HTTP_200_OK)

            logger.error(f"Failed to update hero #{id}. Errors: {serializer.errors}.")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Hero.DoesNotExist:
            logger.error(f"Hero #{id} not found for update.")
            return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=["Heroes"],
        operation_summary="Delete Hero",
        operation_description="Delete a hero by its ID.",
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_PATH, description="ID of the hero to delete", type=openapi.TYPE_INTEGER)
        ],
        responses={
            204: openapi.Response('Hero deleted successfully.'),
            403: openapi.Response(description='User does not have permission to delete the hero.'),
            404: openapi.Response(description='Hero not found.'),
        }
    )
    def delete(self, request, id):
        self.authentication_classes = [IsAdminUser]
        self.check_permissions(request)

        try:
            hero = Hero.objects.get(id=id)
            hero.delete()
            logger.info(f"User {request.user} deleted hero #{id}.")
            return Response({"detail": "Hero deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

        except Hero.DoesNotExist:
            logger.error(f"Hero #{id} not found for deletion.")
            return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)
