from rest_framework import serializers
from default_dota_app.models import ItemSection


class ReadItemSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemSection
        fields=('id', 'section_name', 'img', 'display_order')