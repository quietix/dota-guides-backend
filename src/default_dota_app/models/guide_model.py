from django.db import models
from default_dota_app.models.hero_model import Hero


class Guide(models.Model):
    hero = models.ForeignKey(Hero, null=True, on_delete=models.SET_NULL)
    guide_title = models.CharField(max_length=200)
    guide_description = models.TextField(blank=True)

    def __str__(self):
        return f"<{self.hero.hero_name}> <{self.guide_title}> <guide #{self.id}>"
