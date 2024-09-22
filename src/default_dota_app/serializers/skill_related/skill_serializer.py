from rest_framework import serializers
from default_dota_app.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields=('id', 'skill_name', 'skill_description', 'max_points', 'img')