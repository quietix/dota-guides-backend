from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views as drf_views
from rest_framework.permissions import IsAdminUser
from default_dota_app.serializers.user_serializers import *

import logging

logger = logging.getLogger(__name__)

class UserView(drf_views.APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReadUserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, id):
        try:
            user = User.objects.get(id=id)
            logger.info(f"Attempting to update user: {user.username} (ID: {id})")
        except User.DoesNotExist:
            logger.error(f"User with ID {id} not found for update.")
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            logger.info(f"User {user.username} (ID: {id}) has been successfully updated.")
            return Response(serializer.data, status=status.HTTP_200_OK)

        logger.warning(f"Validation errors occurred while updating user {user.username} (ID: {id}): {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            logger.info(f"Attempting to delete user: {user.username} (ID: {id})")
            user.delete()
            logger.info(f"User {user.username} (ID: {id}) has been successfully deleted.")
            return Response({"detail": "User successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            logger.error(f"User with ID {id} not found for deletion.")
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
