from rest_framework import serializers
from default_dota_app.models import Guide
from default_dota_app.serializers.item_related.stage_serializer import StageSerializer
from default_dota_app.serializers.skill_related.skill_build_serializer import SkillBuildSerializer
from default_dota_app.serializers.user_serializers import ReadUserSerializer


class DetailedGuideSerializer(serializers.ModelSerializer):
    stages = StageSerializer(many=True, read_only=True)
    skill_builds = SkillBuildSerializer(many=True, read_only=True)
    user = ReadUserSerializer(read_only=True)

    class Meta:
        model=Guide
        fields=('user', 'id', 'guide_title', 'guide_description', 'stages', 'skill_builds')
