from django.contrib.auth.models import User
from django.db.models import Prefetch
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from default_dota_app.models import *
from default_dota_app.serializers import *


class HeroesView(APIView):
    def get(self, request):
        heroes = Hero.objects.all().prefetch_related('skills')
        serializer = ReadHeroPreviewSerializer(heroes, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        serializer = WriteHeroSerializer(data=request.data)
        if serializer.is_valid():
            hero = serializer.save()
            return Response(ReadHeroPreviewSerializer(hero).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeroDetailsView(APIView):
    def get(self, request, hero_name):
        if request.user.is_authenticated:
            user_guides = Guide.objects.filter(user=request.user)
        else:
            admin_user = User.objects.filter(is_superuser=True).first()
            user_guides = Guide.objects.filter(user=admin_user)

        prefetch_user_guides = Prefetch('guides', queryset=user_guides)
        hero = Hero.objects.filter(hero_name=hero_name).prefetch_related('skills', prefetch_user_guides).first()

        if not hero:
            return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReadHeroDetailsSerializer(hero)
        return Response(serializer.data)


class HeroSkillsView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, hero_name):
        skills = Skill.objects.filter(hero__hero_name=hero_name)
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
