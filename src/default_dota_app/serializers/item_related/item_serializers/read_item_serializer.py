from rest_framework import serializers

from default_dota_app.models import Item


class ReadItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=('id', 'item_name', 'item_description', 'img')