from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views as drf_views

from default_dota_app.models import *
from default_dota_app.serializers import *


class GuideDetailsView(drf_views.APIView):
    def get(self, request, id):
        if request.user.is_authenticated:
            user = request.user
        else:
            user = User.objects.filter(is_superuser=True).first()

        try:
            guide = Guide.objects.get(user=user, id=id)
            serializer = DetailedGuideSerializer(guide)
            return Response(serializer.data)
        except:
            return Response({"detail:" "Guide with such ID is not found for this user."}, status=status.HTTP_404_NOT_FOUND)
