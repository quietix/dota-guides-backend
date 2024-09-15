from rest_framework import serializers
from default_dota_app.models import Build, Hero

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hero
        fields=('id', 'name', 'img')