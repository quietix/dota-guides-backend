from rest_framework import serializers
from default_dota_app.models import SkillBuild
from default_dota_app.serializers.skill_related.skill_order_serializer import SkillOrderSerializer


class SkillBuildSerializer(serializers.ModelSerializer):
    skills_order = SkillOrderSerializer(many=True, read_only=True)

    class Meta:
        model=SkillBuild
        fields=('id', 'skill_build_name', 'skill_build_description', 'display_order', 'skills_order')