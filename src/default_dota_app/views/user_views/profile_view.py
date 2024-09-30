from rest_framework import status
from rest_framework.response import Response
from rest_framework import views as drf_views
from default_dota_app.auth.admin_or_self_permission import IsAdminOrSelf
from knox.models import AuthToken

from default_dota_app.serializers.user_serializers import *


class ProfileView(drf_views.APIView):
    permission_classes = (IsAdminOrSelf,)

    def get(self, request):
        user = request.user
        serializer = ReadUserSerializer(user)
        return Response(serializer.data)

    def patch(self, request):
        user = request.user

        serializer = UpdateUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        AuthToken.objects.filter(user=user).delete()
        user.delete()
        return Response({"detail": "User successfully deleted."}, status=status.HTTP_204_NO_CONTENT)