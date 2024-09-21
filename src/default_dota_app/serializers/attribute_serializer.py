from rest_framework import serializers
from default_dota_app.models import Attribute


class AttributeSerializer(serializers.ModelSerializer):
    attribute_name = serializers.SerializerMethodField()

    class Meta:
        model = Attribute
        fields = ('id', 'attribute_name', 'img')

    def get_attribute_name(self, obj):
        return dict(obj.ATTRIBUTE_CHOICES).get(obj.attribute_name, obj.attribute_name)
