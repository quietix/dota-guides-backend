from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Max

from default_dota_app.models.guide_model import Guide


def get_next_skill_build_order():
    max_order = SkillBuild.objects.aggregate(Max('display_order'))['display_order__max']
    return (max_order + 1) if max_order is not None else 1


class SkillBuild(models.Model):
    guide = models.ForeignKey(Guide, null=True, on_delete=models.SET_NULL, related_name='skill_builds')
    skill_build_name = models.CharField(max_length=300, default='')
    skill_build_description = models.TextField(blank=True)
    display_order = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return f"<{self.guide.hero.hero_name}> <{self.guide.guide_title}> <{self.skill_build_name}>"

    class Meta:
        ordering = ["guide__hero__hero_name", "guide__display_order", "display_order"]