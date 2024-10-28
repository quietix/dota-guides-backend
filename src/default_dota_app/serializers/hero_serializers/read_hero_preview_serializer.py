from rest_framework import serializers
from default_dota_app.models import Hero
from default_dota_app.serializers.attribute_serializers.read_attribute_serializer import ReadAttributeSerializer


class ReadHeroPreviewSerializer(serializers.ModelSerializer):
    attribute = ReadAttributeSerializer(read_only=True)

    class Meta:
        model = Hero
        fields = ('id', 'hero_name', 'img', 'attribute')
