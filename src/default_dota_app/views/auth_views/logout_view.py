from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from knox import views as knox_views
from rest_framework.response import Response
import logging
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

logger = logging.getLogger(__name__)

class LogoutView(knox_views.LogoutView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=["Authentication"],
        operation_summary="Logout the authenticated user",
        operation_description="This endpoint allows the authenticated user to log out from the current session.",
        responses={
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="Successfully logged out.",
                examples={
                    "application/json": {"message": "Successfully logged out."}
                }
            ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
                description="Unauthorized. Authentication credentials were not provided or are invalid."
            ),
        },
    )
    def post(self, request, format=None):
        response = super(LogoutView, self).post(request, format=None)
        logger.info(f"User {request.user.username} has successfully logged out.")
        return Response({"message": "Successfully logged out."}, status=status.HTTP_204_NO_CONTENT)
