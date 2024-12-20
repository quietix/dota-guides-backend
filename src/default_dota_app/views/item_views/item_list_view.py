from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from default_dota_app.models import *
from default_dota_app.serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging

logger = logging.getLogger(__name__)

class ItemListView(APIView):
    def get_authenticators(self):
        if self.request.method == 'GET':
            return []
        else:
            return super().get_authenticators()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAdminUser()]

    @swagger_auto_schema(
        tags=["Items"],
        operation_description="Retrieve all items or a specific item by ID",
        responses={
            200: openapi.Response('Success', ReadItemBySectionsSerializer(many=True)),
            404: 'Item not found'
        }
    )
    def get(self, request):
        logger.info("Getting all items")
        item_sections = ItemSection.objects.all().prefetch_related('items')
        serializer = ReadItemBySectionsSerializer(item_sections, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        tags=["Items"],
        operation_description="Create a new item (Admin only)",
        request_body=UpsertItemSerializer,
        responses={
            201: ReadItemSerializer,
            400: 'Invalid input'
        }
    )
    def post(self, request):
        serializer = UpsertItemSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            logger.info(f"Created item #{item.id}")
            return Response(ReadItemSerializer(item).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
