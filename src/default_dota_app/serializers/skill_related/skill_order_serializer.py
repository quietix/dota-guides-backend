from rest_framework import serializers

from default_dota_app.models import SkillOrder


class SkillOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=SkillOrder
        fields=('id', 'learning_order', 'skill')