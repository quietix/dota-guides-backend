from rest_framework import status
from rest_framework.response import Response
from rest_framework import views as drf_views
from default_dota_app.auth.admin_or_self_permission import IsAdminOrSelf
from knox.models import AuthToken
from default_dota_app.serializers.user_serializers import *
import logging

logger = logging.getLogger(__name__)

class ProfileView(drf_views.APIView):
    permission_classes = (IsAdminOrSelf,)

    def get(self, request):
        user = request.user
        serializer = ReadUserSerializer(user)
        return Response(serializer.data)

    def patch(self, request):
        user = request.user
        logger.info(f"Attempting to update profile for user: {user.username} (ID: {user.id})")

        serializer = UpdateUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            logger.info(f"Profile updated successfully for user: {user.username} (ID: {user.id})")
            return Response(serializer.data, status=status.HTTP_200_OK)

        logger.warning(f"Validation errors occurred while updating profile for user {user.username} (ID: {user.id}): {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        logger.info(f"Attempting to delete profile for user: {user.username} (ID: {user.id})")

        AuthToken.objects.filter(user=user).delete()
        user.delete()

        logger.info(f"Profile successfully deleted for user: {user.username} (ID: {user.id})")
        return Response({"detail": "User successfully deleted."}, status=status.HTTP_204_NO_CONTENT)