from rest_framework import serializers
from default_dota_app.models import Item, ItemSection


class CreateItemSerializer(serializers.ModelSerializer):
    item_section = serializers.SlugRelatedField(
        queryset=ItemSection.objects.all(),
        slug_field='section_name'
    )

    class Meta:
        model=Item
        fields=('item_section', 'item_name', 'item_description', 'img')