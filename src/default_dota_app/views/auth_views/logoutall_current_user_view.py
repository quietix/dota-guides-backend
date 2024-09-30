from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from knox import views as knox_views
from rest_framework.response import Response


class LogoutAllCurrentUserSessionsView(knox_views.LogoutAllView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        response = super(LogoutAllCurrentUserSessionsView, self).post(request, format=None)
        return Response({"message": "Successfully logged out from all sessions."}, status=status.HTTP_204_NO_CONTENT)