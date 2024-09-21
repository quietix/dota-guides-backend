from rest_framework import serializers
from default_dota_app.models import Attribute


class HeroSerializer(serializers.ModelSerializer):
    attribute_name = serializers.SerializerMethodField()

    class Meta:
        model = Attribute
        fields = ('id', 'attribute_name', 'img')

    def get_attribute(self, obj):
        return obj.get_attribute_display()
