from rest_framework.permissions import AllowAny
from rest_framework import status
from default_dota_app.serializers.auth import *
from knox import views as knox_views
from rest_framework.response import Response
from django.contrib.auth import login
from drf_yasg.utils import swagger_auto_schema
import logging
from drf_yasg import openapi

logger = logging.getLogger(__name__)

class LoginView(knox_views.LoginView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        tags=["Authentication"],
        operation_summary="User Login",
        operation_description="Logs in a user and returns an authentication token.",
        request_body=LoginSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Successfully logged in.",
                examples={
                    "application/json": {
                        "token": "your_auth_token_here"
                    }
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid credentials.",
                examples={
                    "application/json": {
                        "Authentication Failed": "Email or password is wrong."
                    }
                }
            ),
        },
    )
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=False):
            user = serializer.validated_data['user']
            login(request, user)
            logger.info(f"Successful login attempt for user: {user.username}")
            return super(LoginView, self).post(request, format=None)
        else:
            logger.warning(f"Unsuccessful login attempt. errors: {serializer.errors}")
            errors = serializer.errors

            if 'non_field_errors' in errors:
                errors.pop('non_field_errors')
                return Response({'Authentication Failed': "Email or password is wrong."}, status=status.HTTP_400_BAD_REQUEST)

            return Response(errors, status=status.HTTP_400_BAD_REQUEST)