from django.db import models
from default_dota_app.models.attribute_model import Attribute


class Hero(models.Model):
    hero_name = models.CharField(max_length=200, unique=True)
    attribute = models.ForeignKey(Attribute, null=True, on_delete=models.SET_NULL)
    img = models.ImageField(null=True, blank=True, upload_to='heroes')

    def __str__(self):
        return f"{self.hero_name}"

    class Meta:
        ordering = ["hero_name"]
