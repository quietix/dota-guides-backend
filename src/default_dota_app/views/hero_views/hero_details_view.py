from django.contrib.auth.models import User
from django.db.models import Prefetch
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from default_dota_app.models import *
from default_dota_app.serializers.hero_serializers import *
from default_dota_app.services import HeroService
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
            200: openapi.Response('Successful retrieval of hero details'),
            404: openapi.Response(description='Hero not found.'),
        }
    )
    def get(self, request, id):
        user = request.user
        hero_data = HeroService.get_hero_details(id, user)

        if hero_data is None:
            return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response(hero_data, status=status.HTTP_200_OK)

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
            200: openapi.Response('Hero updated successfully', ReadHeroDetailsAsAdminSerializer),
            400: openapi.Response(description='Invalid input data.'),
            403: openapi.Response(description='User does not have permission to update the hero.'),
            404: openapi.Response(description='Hero not found.'),
        }
    )
    def patch(self, request, id):
        self.authentication_classes = [IsAdminUser]
        self.check_permissions(request)

        updated_hero = HeroService.patch_hero(request, id)

        if updated_hero:
            logger.info(f"User {request.user} updated details for hero #{id}.")
            return Response(updated_hero, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Update failed."}, status=status.HTTP_400_BAD_REQUEST)

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

        is_delete_succeeded = HeroService.delete_hero(request, id)

        if is_delete_succeeded:
            return Response({f"Hero #{id} is successfully deleted."})
        return Response({"detail": "Delete failed."}, status=status.HTTP_400_BAD_REQUEST)
