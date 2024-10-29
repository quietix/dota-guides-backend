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

class ItemDetailsView(APIView):
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
        operation_description="Retrieve specific item by ID",
        responses={
            200: openapi.Response('Success', ReadItemBySectionsSerializer(many=True)),
            404: 'Item not found'
        }
    )
    def get(self, request, id):
        try:
            item = Item.objects.get(id=id)
        except Item.DoesNotExist:
            logger.error(f"User {request.user.username} failed to retrieve item #{id}.")
            return Response({"error": f"Item #{id} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReadItemSerializer(item)

        logger.info(f"Retrieved item #{item.id}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Items"],
        operation_description="Update an existing item (Admin only)",
        request_body=UpsertItemSerializer,
        responses={
            200: ReadItemSerializer,
            400: 'Invalid input',
            404: 'Item not found'
        }
    )
    def patch(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        try:
            item = Item.objects.get(id=id)
        except Item.DoesNotExist:
            logger.error(f"User {request.user.username} failed to update item #{id}. Item #{id} does not exist.")
            return Response({"error": f"Item #{id} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UpsertItemSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            updated_item = serializer.save()
            logger.info(f"Updated item #{updated_item.id}")
            return Response(ReadItemSerializer(updated_item).data, status=status.HTTP_200_OK)

        logger.error(f"User {request.user.username} failed to update item #{id}. Errors: {serializer.errors}.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["Items"],
        operation_description="Delete an item (Admin only)",
        responses={
            204: 'Item deleted successfully',
            404: 'Item not found'
        }
    )
    def delete(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        try:
            item = Item.objects.get(id=id)
        except Item.DoesNotExist:
            logger.error(f"User {request.user.username} failed to delete item #{id}")
            return Response({"error": f"Item #{id} not found"}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        logger.info(f"User {request.user.username} deleted item #{id}")
        return Response({"message": f"Item {id} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)