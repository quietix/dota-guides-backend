from rest_framework import serializers
from default_dota_app.models import Guide
from default_dota_app.serializers.item_related.stage_serializer import StageSerializer
from default_dota_app.serializers.skill_related.skill_build_serializer import SkillBuildSerializer


class DetailedGuideSerializer(serializers.ModelSerializer):
    stages = StageSerializer(many=True, read_only=True)
    skill_builds = SkillBuildSerializer(many=True, read_only=True)

    class Meta:
        model=Guide
        fields=('id', 'guide_title', 'guide_description', 'stages', 'skill_builds')