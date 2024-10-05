from rest_framework import serializers
from default_dota_app.models import Hero, Attribute


class UpsertHeroSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False)
    attribute = serializers.SlugRelatedField(
        queryset=Attribute.objects.all(),
        slug_field='attribute_name'
    )

    class Meta:
        model = Hero
        fields = ('hero_name', 'img', 'attribute')