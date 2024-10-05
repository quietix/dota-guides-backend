from rest_framework import serializers
from default_dota_app.models import Guide


class PreviewGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guide
        fields=('id', 'guide_title', 'guide_description')
