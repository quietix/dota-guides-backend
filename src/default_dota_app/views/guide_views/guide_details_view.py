from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views as drf_views
from rest_framework.permissions import IsAuthenticated

from default_dota_app.models import *
from default_dota_app.serializers import *


class GuideDetailsView(drf_views.APIView):
    def get_user(self, request):
        if request.user.is_authenticated:
            return request.user
        else:
            return User.objects.filter(is_superuser=True).first()

    def get(self, request, id):
        user = self.get_user(request)
        try:
            guide = Guide.objects.get(user=user, id=id)
            serializer = DetailedGuideSerializer(guide)
            return Response(serializer.data)
        except Guide.DoesNotExist:
            return Response({"detail:" "Guide with such ID is not found for this user."}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        permission_classes = (IsAuthenticated,)
        user = self.get_user(request)
        try:
            guide = Guide.objects.get(user=user, id=id)
            serializer = UpdateGuideSerializer(guide, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Guide.DoesNotExist:
            return Response({"detail": "Guide with such ID is not found for this user."},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        user = self.get_user(request)
        try:
            guide = Guide.objects.get(user=user, id=id)
            guide.delete()
            return Response({"detail": "Guide successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Guide.DoesNotExist:
            return Response({"detail": "Guide with such ID is not found for this user."},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": e}, status=status.HTTP_400_BAD_REQUEST)