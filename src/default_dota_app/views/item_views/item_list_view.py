from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from default_dota_app.models import *
from default_dota_app.serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging

logger = logging.getLogger(__name__)

class ItemListView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=["Items"],
        operation_description="Retrieve all items or a specific item by ID",
        responses={
            200: openapi.Response('Success', ListItemsBySectionsSerializer(many=True)),
            404: 'Item not found'
        }
    )
    def get(self, request):
        logger.info("Getting all items")
        item_sections = ItemSection.objects.all().prefetch_related('items')
        serializer = ListItemsBySectionsSerializer(item_sections, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        tags=["Items"],
        operation_description="Create a new item (Admin only)",
        request_body=CreateItemSerializer,
        responses={
            201: ReadItemSerializer,
            400: 'Invalid input'
        }
    )
    def post(self, request):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        serializer = CreateItemSerializer(data=request.data)

        if serializer.is_valid():
            item = serializer.save()
            logger.info(f"Created item #{item.id}")
            return Response(ReadItemSerializer(item).data, status=status.HTTP_201_CREATED)

        logger.error(f"User {request.user.username} failed to create an item. Errors: {serializer.errors}.")
        return Response(f"User {request.user.username} failed to create an item. Errors: {serializer.errors}.",
                        status=status.HTTP_400_BAD_REQUEST)
