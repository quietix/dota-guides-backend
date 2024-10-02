from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views as drf_views
from rest_framework.permissions import IsAuthenticated

from default_dota_app.models import *
from default_dota_app.serializers import *
import logging


logger = logging.getLogger(__name__)

class GuideDetailsView(drf_views.APIView):
    def get_user_or_admin(self, request):
        if request.user.is_authenticated:
            return request.user
        else:
            return User.objects.filter(is_superuser=True).first()

    def get(self, request, id):
        user = self.get_user_or_admin(request)
        try:
            guide = Guide.objects.get(user=user, id=id)
            serializer = DetailedGuideSerializer(guide)
            return Response(serializer.data)
        except Guide.DoesNotExist:
            return Response({"detail:" "Guide with such ID is not found for this user."}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        user = request.user

        try:
            guide = Guide.objects.get(user=user, id=id)
            serializer = UpdateGuideSerializer(guide, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                logger.info(f"User {user} has updated Guide #{id}")
                return Response(serializer.data, status=status.HTTP_200_OK)

            logger.error(f"User {user} has failed to update Guide #{id}. Errors: {serializer.errors}.")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Guide.DoesNotExist:
            logger.error(f"User {user} has failed to update Guide #{id}. Guide #{id} does not exist.")
            return Response({"detail": "Guide with such ID is not found for this user."},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        user = request.user

        try:
            guide = Guide.objects.get(user=user, id=id)
            guide.delete()
            return Response({"detail": "Guide successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Guide.DoesNotExist:
            return Response({"detail": "Guide with such ID is not found for this user."},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": e}, status=status.HTTP_400_BAD_REQUEST)