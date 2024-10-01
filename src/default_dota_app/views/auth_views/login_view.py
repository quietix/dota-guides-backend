from rest_framework.permissions import AllowAny
from rest_framework import status
from default_dota_app.serializers.auth import *
from knox import views as knox_views
from rest_framework.response import Response
from django.contrib.auth import login
import logging

logger = logging.getLogger(__name__)

class LoginView(knox_views.LoginView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            logger.info(f"Successful login attempt for user: {user.username}")
            return super(LoginView, self).post(request, format=None)
        else:
            logger.warning(f"Unsuccessful login attempt for user: {username}, errors: {serializer.errors}")
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
