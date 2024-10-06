from rest_framework import serializers
from default_dota_app.models import Guide
from default_dota_app.models import Hero


class UpsertGuideSerializer(serializers.ModelSerializer):
    hero = serializers.SlugRelatedField(
        queryset=Hero.objects.all(),
        slug_field='hero_name'
    )

    class Meta:
        model=Guide
        fields=('hero', 'user', 'display_order', 'guide_title', 'guide_description')
