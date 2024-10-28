from rest_framework.permissions import IsAdminUser
from rest_framework import status
from knox import views as knox_views
from rest_framework.response import Response
from knox.models import AuthToken
import logging
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

logger = logging.getLogger(__name__)

class LogoutAllUsersView(knox_views.LogoutAllView):
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(
        tags=["Admin Actions: Users"],
        operation_summary="Logout all users (admin only)",
        operation_description="This endpoint allows an admin to log out all users by deleting all active authentication tokens.",
        responses={
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="Successfully logged out all users.",
                examples={
                    "application/json": {"message": "Successfully logged out all users."}
                }
            ),
            status.HTTP_403_FORBIDDEN: openapi.Response(
                description="Forbidden. Only admins are allowed to perform this action."
            ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
                description="Unauthorized. Authentication credentials were not provided or are invalid."
            ),
        },
    )
    def post(self, request, format=None):
        AuthToken.objects.all().delete()
        logger.info(f"User {request.user.username} has successfully logged out all users.")
        return Response({"message": "Successfully logged out all users."}, status=status.HTTP_204_NO_CONTENT)
