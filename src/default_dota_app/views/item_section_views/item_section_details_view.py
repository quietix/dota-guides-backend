from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from default_dota_app.models import *
from default_dota_app.serializers import *
from drf_yasg.utils import swagger_auto_schema
import logging

logger = logging.getLogger(__name__)

class ItemSectionDetailsView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=["Item Section"],
        operation_description="Retrieve specific Item Section by ID",
        responses={
            200: ReadItemSectionSerializer,
            404: 'Item Section not found'
        }
    )
    def get(self, request, id):
        try:
            item_section = ItemSection.objects.get(id=id)
        except ItemSection.DoesNotExist:
            logger.error(f"User {request.user.username} failed to retrieve Item Section #{id}.")
            return Response({"error": "Item Section not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReadItemSectionSerializer(item_section)
        logger.info(f"Retrieved Item Section #{item_section.id}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Item Section"],
        operation_description="Update an existing item section (Admin only)",
        request_body=UpsertItemSectionSerializer,
        responses={
            200: ReadItemSectionSerializer,
            400: 'Invalid input',
            404: 'Item Section not found'
        }
    )
    def patch(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        try:
            item_section = ItemSection.objects.get(id=id)
        except ItemSection.DoesNotExist:
            logger.error(f"User {request.user.username} failed to update Item Section #{id}. Item Section #{id} does not exist.")
            return Response({"error": f"Item Section #{id} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UpsertItemSectionSerializer(item_section, data=request.data, partial=True)

        if serializer.is_valid():
            updated_item_section = serializer.save()
            logger.info(f"Updated Item Section #{updated_item_section.id}")
            return Response(ReadItemSectionSerializer(updated_item_section).data, status=status.HTTP_200_OK)

        logger.error(f"User {request.user.username} failed to update Item Section #{id}. Errors: {serializer.errors}.")
        return Response(f"User {request.user.username} failed to update Item Section #{id}. Errors: {serializer.errors}.",
                        status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["Item Section"],
        operation_description="Delete an item section (Admin only)",
        responses={
            204: 'Item Section deleted successfully',
            404: 'Item Section not found'
        }
    )
    def delete(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        try:
            item_section = ItemSection.objects.get(id=id)
        except ItemSection.DoesNotExist:
            logger.error(f"User {request.user.username} failed to delete Item Section #{id}. Item Section #{id} does not exist.")
            return Response({"error": f"Item Section #{id} not found"}, status=status.HTTP_404_NOT_FOUND)

        item_section.delete()
        logger.info(f"User {request.user.username} deleted Item Section #{id}")
        return Response({"message": f"Item Section #{id} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

