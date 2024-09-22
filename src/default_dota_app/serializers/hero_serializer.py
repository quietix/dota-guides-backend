from rest_framework import serializers
from default_dota_app.models import Hero
from default_dota_app.serializers.attribute_serializer import AttributeSerializer
from default_dota_app.serializers.skill_related.skill_serializer import SkillSerializer


class HeroSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = ('id', 'hero_name', 'img', 'attribute', 'skills')
