from rest_framework import serializers
from default_dota_app.models import Hero
from default_dota_app.serializers.skill_related import SkillSerializer
from default_dota_app.serializers.attribute_serializer import AttributeSerializer
from default_dota_app.serializers.guide_serializers import PreviewGuideSerializer


class ReadHeroDetailsAsAdminSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    guides = PreviewGuideSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = ('id', 'hero_name', 'img', 'attribute', 'skills', 'guides')
