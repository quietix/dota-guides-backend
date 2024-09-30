from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from default_dota_app.models import *
from default_dota_app.serializers import *


class GuidesView(APIView):
    def get(self, request, hero_name):
        try:
            hero = Hero.objects.get(hero_name=hero_name)
        except:
            return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user.is_authenticated:
            guides = Guide.objects.filter(user=request.user, hero__hero_name=hero_name)
        else:
            admin_user = User.objects.filter(is_superuser=True).first()
            guides = Guide.objects.filter(user=admin_user, hero__hero_name=hero_name)

        serializer = DetailedGuideSerializer(guides, many=True)
        return Response(serializer.data)

    def post(self, request, hero_name):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        try:
            hero = Hero.objects.get(hero_name=hero_name)
        except:
            return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['hero'] = hero.hero_name

        serializer = WriteGuideSerializer(data=data)

        if serializer.is_valid():
            guide = serializer.save(user=self.request.user)
            return Response(PreviewGuideSerializer(guide).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuideDetailsView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, guide_id):
        guides = Guide.objects.filter(id=guide_id).prefetch_related('stages__item_wrappers__item')
        if not guides.exists():
            return Response({"detail": "Guide not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = DetailedGuideSerializer(guides, many=True)
        return Response(serializer.data)
