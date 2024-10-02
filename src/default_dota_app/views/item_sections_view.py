from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from default_dota_app.models import *
from default_dota_app.serializers import *
import logging

logger = logging.getLogger(__name__)

class ItemSectionsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id=None):
        if id:
            return self.get_item_section(request, id)

        logger.info("Getting all Item Sections")
        item_sections = ItemSection.objects.all()
        serializer = ListItemSectionsSerializer(item_sections, many=True)
        return Response(serializer.data)

    def get_item_section(self, request, id):
        try:
            item_section = ItemSection.objects.get(id=id)
        except ItemSection.DoesNotExist:
            logger.error(f"User {request.user.username} failed to retrieve Item Section #{id}.")
            return Response({"error": "Item Section not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ListItemSectionsSerializer(item_section)

        logger.info(f"Retrieved Item Section #{item_section.id}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        serializer = CreateItemSectionSerializer(data=request.data)

        if serializer.is_valid():
            item_section = serializer.save()
            logger.info(f"Created Item Section #{item_section.id}")
            return Response(ListItemSectionsSerializer(item_section).data, status=status.HTTP_201_CREATED)

        logger.error(f"User {request.user.username} failed to create an Item Section. Errors: {serializer.errors}.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        try:
            item_section = ItemSection.objects.get(id=id)
        except ItemSection.DoesNotExist:
            logger.error(f"User {request.user.username} failed to update Item Section #{id}. Item Section #{id} does not exist.")
            return Response({"error": f"Item Section #{id} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateItemSectionSerializer(item_section, data=request.data, partial=True)

        if serializer.is_valid():
            updated_item_section = serializer.save()
            logger.info(f"Updated Item Section #{updated_item_section.id}")
            return Response(ListItemSectionsSerializer(updated_item_section).data, status=status.HTTP_200_OK)

        logger.error(f"User {request.user.username} failed to update Item Section #{id}. Errors: {serializer.errors}.")
        return Response(f"User {request.user.username} failed to update Item Section #{id}. Errors: {serializer.errors}.",
                        status=status.HTTP_400_BAD_REQUEST)

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