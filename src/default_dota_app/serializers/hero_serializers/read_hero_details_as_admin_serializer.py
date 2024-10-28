from rest_framework import serializers
from default_dota_app.models import Hero
from default_dota_app.serializers.skill_related import SkillSerializer
from default_dota_app.serializers.attribute_serializers.read_attribute_serializer import ReadAttributeSerializer
from default_dota_app.serializers.guide_serializers import PreviewGuideSerializer


class ReadHeroDetailsAsAdminSerializer(serializers.ModelSerializer):
    attribute = ReadAttributeSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    admin_guides = PreviewGuideSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = ('id', 'hero_name', 'img', 'attribute', 'skills', 'admin_guides')
