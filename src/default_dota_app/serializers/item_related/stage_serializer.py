from rest_framework import serializers
from default_dota_app.serializers.item_related.item_wrapper_serializer import ItemWrapperSerializer
from default_dota_app.models import Stage


class StageSerializer(serializers.ModelSerializer):
    item_wrappers = ItemWrapperSerializer(many=True, read_only=True)
    print(item_wrappers.data)

    class Meta:
        model = Stage
        fields = ('stage_name', 'description', 'item_wrappers')
