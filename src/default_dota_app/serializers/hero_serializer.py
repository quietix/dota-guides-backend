from rest_framework import serializers
from default_dota_app.models import Hero


class HeroSerializer(serializers.ModelSerializer):
    attribute = serializers.SerializerMethodField()

    class Meta:
        model = Hero
        fields = ('hero_name', 'attribute', 'img')

    def get_attribute(self, obj):
        return obj.get_attribute_display()
