from rest_framework import serializers
from default_dota_app.models import Hero

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hero
        fields=('hero_name', 'attribute', 'img')

