from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from knox import views as knox_views
from rest_framework.response import Response
import logging
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

logger = logging.getLogger(__name__)

class LogoutAllCurrentUserSessionsView(knox_views.LogoutAllView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=["Authentication"],
        operation_summary="Logout all sessions for the authenticated user",
        operation_description="This endpoint allows the authenticated user to log out from all active sessions.",
        responses={
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="Successfully logged out from all sessions.",
                examples={
                    "application/json": {"message": "Successfully logged out from all sessions."}
                }
            ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
                description="Unauthorized. Authentication credentials were not provided or invalid."
            ),
        },
    )
    def post(self, request, format=None):
        response = super(LogoutAllCurrentUserSessionsView, self).post(request, format=None)
        logger.info(f"User {request.user.username} has successfully logged out all their sessions.")
        return Response({"message": "Successfully logged out from all sessions."}, status=status.HTTP_204_NO_CONTENT)
