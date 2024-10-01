from rest_framework import serializers
from default_dota_app.models import ItemSection
from default_dota_app.serializers.item_related.item_serializer import ItemSerializer


class ItemSectionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model=ItemSection
        fields=('id', 'section_name', 'img', 'display_order', 'items')