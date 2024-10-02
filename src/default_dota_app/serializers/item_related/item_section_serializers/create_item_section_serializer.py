from rest_framework import serializers
from default_dota_app.models import ItemSection


class CreateItemSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemSection
        fields=('section_name', 'img', 'display_order')