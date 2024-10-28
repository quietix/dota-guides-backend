from rest_framework import serializers
from default_dota_app.models import Attribute


class ReadAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'attribute_name', 'img', 'display_order')
