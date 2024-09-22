from django.db import models
from django.core.validators import MinValueValidator
from default_dota_app.models.skill_related.skill_model import Skill
from default_dota_app.models.skill_related.skill_build_model import SkillBuild


class SkillOrder(models.Model):
    skill_build = models.ForeignKey(SkillBuild, null=True, on_delete=models.SET_NULL, related_name='skills_order')
    learning_order = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ]
    )
    skill = models.ForeignKey(Skill, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"<{self.skill_build.guide.hero.hero_name}> " \
               f"<{self.skill_build.guide.guide_title}> " \
               f"<{self.skill_build.skill_build_name}> " \
               f"<Skill Order #{self.id}>"
