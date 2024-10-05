from rest_framework import serializers
from default_dota_app.models import Hero
from default_dota_app.serializers.attribute_serializer import AttributeSerializer


class ReadHeroPreviewSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True)

    class Meta:
        model = Hero
        fields = ('id', 'hero_name', 'img', 'attribute')
