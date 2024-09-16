from rest_framework import serializers
from default_dota_app.models import TalentWrapper
from default_dota_app.serializers.talent_related.talent_serializer import TalentSerializer

class TalentWrapperSerializer(serializers.ModelSerializer):
    talent = TalentSerializer(read_only=True)

    class Meta:
        model=TalentWrapper
        fields=('talent', 'explanation')
