from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views as drf_views
from rest_framework.permissions import IsAdminUser

from default_dota_app.models import *
from default_dota_app.serializers.user_serializers import *


class GetAllUsersView(drf_views.APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        users = User.objects.all()
        serializer = ReadUserSerializer(users, many=True)
        return Response(serializer.data)
