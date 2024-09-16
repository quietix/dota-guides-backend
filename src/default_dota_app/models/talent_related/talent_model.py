from django.db import models
from default_dota_app.models.hero_model import Hero

class Talent(models.Model):
    description = models.TextField()
    is_left = models.BooleanField()
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.hero} {self.description}"

    class Meta:
        ordering = ["hero", "id"]