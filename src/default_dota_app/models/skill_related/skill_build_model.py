from django.db import models
from default_dota_app.models.guide_model import Guide
from default_dota_app.models.skill_related.skill_model import Skill


class SkillBuild(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True, related_name='skillbuilds')
    description = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        if self.guide:
            return f"Skill Build {self.id} of Guide {self.guide.id}"
        else:
            return f"Skill Build {self.id} (No Guide)"