from rest_framework import serializers
from default_dota_app.models import ItemWrapper
from default_dota_app.serializers.item_related.item_serializer import ItemSerializer


class ItemWrapperSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model=ItemWrapper
        fields=('id', 'item', 'item_wrapper_explanation')