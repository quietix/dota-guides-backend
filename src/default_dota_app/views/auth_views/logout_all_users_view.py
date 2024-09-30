from rest_framework.permissions import IsAdminUser
from rest_framework import status
from knox import views as knox_views
from rest_framework.response import Response
from knox.models import AuthToken


class LogoutAllUsersView(knox_views.LogoutAllView):
    permission_classes = (IsAdminUser,)

    def post(self, request, format=None):
        AuthToken.objects.all().delete()
        return Response({"message": "Successfully logged out all users."}, status=status.HTTP_204_NO_CONTENT)
