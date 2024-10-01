from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from knox import views as knox_views
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

class LogoutView(knox_views.LogoutView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        response = super(LogoutView, self).post(request, format=None)
        logger.info(f"User {request.user.username} has successfully logged out.")
        return Response({"message": "Successfully logged out."}, status=status.HTTP_204_NO_CONTENT)
