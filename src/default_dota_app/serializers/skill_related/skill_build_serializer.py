from rest_framework import serializers
from default_dota_app.models import SkillBuild
from default_dota_app.serializers.skill_related.skill_serializer import SkillSerializer


class SkillBuildSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model=SkillBuild
        fields=('description', 'skills')
