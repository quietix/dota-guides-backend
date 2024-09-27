from rest_framework import serializers
from default_dota_app.models import Hero, Attribute
from default_dota_app.serializers.attribute_serializer import AttributeSerializer
from default_dota_app.serializers.skill_related.skill_serializer import SkillSerializer
from default_dota_app.serializers.guide_serializer import PreviewGuideSerializer


class ReadHeroPreviewSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True)

    class Meta:
        model = Hero
        fields = ('id', 'hero_name', 'img', 'attribute')


class ReadHeroDetailsSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    guides = PreviewGuideSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = ('id', 'hero_name', 'img', 'attribute', 'skills', 'guides')


class WriteHeroSerializer(serializers.ModelSerializer):
    attribute = serializers.PrimaryKeyRelatedField(queryset=Attribute.objects.all())

    class Meta:
        model = Hero
        fields = (
            'hero_name',
            'img',
            'attribute',
        )