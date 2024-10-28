from rest_framework import serializers
from default_dota_app.models import Attribute


class UpsertAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('attribute_name', 'img', 'display_order')
