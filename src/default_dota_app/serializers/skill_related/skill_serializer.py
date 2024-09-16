from rest_framework import serializers
from default_dota_app.models import Skill
from default_dota_app.serializers.hero_serializer import HeroSerializer

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields=('skill_name', 'skill_description', 'max_points', 'img')
