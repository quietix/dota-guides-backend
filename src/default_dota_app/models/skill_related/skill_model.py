from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from default_dota_app.models.hero_model import Hero


class Skill(models.Model):
    hero = models.ForeignKey(Hero, null=True, on_delete=models.SET_NULL, related_name='skills')
    skill_name = models.CharField(max_length=300)
    skill_description = models.TextField(blank=True)
    max_points = models.IntegerField(
        default=4,
        validators=[
            MaxValueValidator(7),
            MinValueValidator(1)
        ]
    )
    img = models.ImageField(null=True, blank=True, upload_to='skills')
    skill_order = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(6),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return f"<{self.hero}> <{self.skill_name}> <Skill #{self.skill_order}>"

    class Meta:
        ordering = ["hero__hero_name", "skill_order"]
