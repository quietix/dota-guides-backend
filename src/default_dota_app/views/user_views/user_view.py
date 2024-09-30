from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views as drf_views
from rest_framework.permissions import IsAdminUser

from default_dota_app.serializers.user_serializers import *


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
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
