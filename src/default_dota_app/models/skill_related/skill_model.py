from django.db import models
from default_dota_app.models.hero_model import Hero


class Skill(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, null=True)
    skill_name = models.CharField(max_length=200)
    skill_description = models.TextField(blank=True)
    max_points = models.SmallIntegerField()
    img = models.ImageField(null=True, blank=True, upload_to='skills')

    def __str__(self):
        return f"{self.hero} {self.skill_description}"

    class Meta:
        ordering = ["hero", "skill_name"]
