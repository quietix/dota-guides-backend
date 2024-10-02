from rest_framework import serializers
from default_dota_app.models import ItemSection
from default_dota_app.serializers.item_related.item_serializers.read_item_serializer import ReadItemSerializer


class ListItemsBySectionsSerializer(serializers.ModelSerializer):
    items = ReadItemSerializer(many=True)

    class Meta:
        model=ItemSection
        fields=('id', 'section_name', 'img', 'display_order', 'items')