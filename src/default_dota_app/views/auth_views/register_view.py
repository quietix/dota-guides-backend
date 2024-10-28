from default_dota_app.serializers import RegisterSerializer
from default_dota_app.repositories import UserRepository
from default_dota_app.auth.is_authenticated_manual_check import IsAuthenticatedManualCheck
from rest_framework import views as drf_views
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging

logger = logging.getLogger(__name__)

class RegisterView(drf_views.APIView):
    authentication_classes = [IsAuthenticatedManualCheck]

    @swagger_auto_schema(
        tags=["Authentication"],
        request_body=RegisterSerializer,
        responses={
            201: openapi.Response(description="User successfully registered", schema=RegisterSerializer),
            400: "Invalid input data"
        },
        operation_summary="Register a new user",
        operation_description="Create a new user account with the provided credentials.",
    )
    def post(self, request):
        if UserRepository.is_user_authed(request):
            return Response({"details": "Authorized user cannot register."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

