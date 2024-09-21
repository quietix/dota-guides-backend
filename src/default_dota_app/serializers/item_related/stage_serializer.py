from rest_framework import serializers
from default_dota_app.models import Stage
from default_dota_app.serializers.item_related.item_wrapper_serializer import ItemWrapperSerializer


class StageSerializer(serializers.ModelSerializer):
    item_wrappers = ItemWrapperSerializer(many=True, read_only=True)

    class Meta:
        model=Stage
        fields=('id', 'stage_name', 'stage_description', 'item_wrappers')