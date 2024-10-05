from rest_framework import serializers

from default_dota_app.models import ItemWrapper
from default_dota_app.serializers.item_related.item_serializers.read_item_serializer import ReadItemSerializer


class ItemWrapperSerializer(serializers.ModelSerializer):
    item = ReadItemSerializer(read_only=True)

    class Meta:
        model=ItemWrapper
        fields=('id', 'item', 'item_wrapper_explanation')