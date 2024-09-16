from rest_framework import serializers
from default_dota_app.models import Talent
from default_dota_app.serializers.hero_serializer import HeroSerializer


class TalentSerializer(serializers.ModelSerializer):
    hero = HeroSerializer(read_only=True)

    class Meta:
        model=Talent
        fields=('description', 'is_left', 'hero')
