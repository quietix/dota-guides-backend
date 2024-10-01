from django.contrib.auth.models import User
from rest_framework import generics
from default_dota_app.serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        logger.info(f"Registration attempt for data: {request.data}")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        logger.info(f"User {user.username} has been successfully registered.")

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
