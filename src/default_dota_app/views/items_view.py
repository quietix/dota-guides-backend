from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from default_dota_app.models import *
from default_dota_app.serializers import *
import logging

logger = logging.getLogger(__name__)

class ItemsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id=None):
        if id:
            return self.get_item(request, id)

        logger.info("Getting all items")
        item_sections = ItemSection.objects.all().prefetch_related('items')
        serializer = ListItemsBySectionsSerializer(item_sections, many=True)
        return Response(serializer.data)

    def get_item(self, request, id):
        try:
            item = Item.objects.get(id=id)
        except Item.DoesNotExist:
            logger.error(f"User {request.user.username} failed to retrieve item #{id}.")
            return Response({"error": f"Item #{id} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReadItemSerializer(item)

        logger.info(f"Retrieved item #{item.id}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        serializer = CreateItemSerializer(data=request.data)

        if serializer.is_valid():
            item = serializer.save()
            logger.info(f"Created item #{item.id}")
            return Response(ReadItemSerializer(item).data, status=status.HTTP_201_CREATED)

        logger.error(f"User {request.user.username} failed to create an item. Errors: {serializer.errors}.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        try:
            item = Item.objects.get(id=id)
        except Item.DoesNotExist:
            logger.error(f"User {request.user.username} failed to update item #{id}. Item #{id} does not exist.")
            return Response({"error": f"Item #{id} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateItemSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            updated_item = serializer.save()
            logger.info(f"Updated item #{updated_item.id}")
            return Response(ReadItemSerializer(updated_item).data, status=status.HTTP_200_OK)

        logger.error(f"User {request.user.username} failed to update item #{id}. Errors: {serializer.errors}.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        try:
            item = Item.objects.get(id=id)
        except Item.DoesNotExist:
            logger.error(f"User {request.user.username} failed to delete item #{id}")
            return Response({"error": f"Item #{id} not found"}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        logger.info(f"User {request.user.username} deleted item #{item.id}")
        return Response({"message": f"Item {item.id} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)