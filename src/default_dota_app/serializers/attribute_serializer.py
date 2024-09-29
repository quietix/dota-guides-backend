from rest_framework import serializers

from default_dota_app.models import Attribute


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'attribute_name', 'img')
