from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import views as drf_views

from default_dota_app.models import *
from default_dota_app.serializers import *


class CreateGuideView(drf_views.APIView):
    def post(self, request, hero_name):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        try:
            hero = Hero.objects.get(hero_name=hero_name)
        except:
            return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['hero'] = hero.hero_name

        serializer = CreateGuideSerializer(data=data)

        if serializer.is_valid():
            guide = serializer.save(user=request.user)
            return Response(PreviewGuideSerializer(guide).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
