from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Build(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    items = ArrayField(models.CharField(max_length=200, blank=True), size=6)

    def __str__(self):
        return f"{self.hero}. Build id {self.id} "

    class Meta:
        ordering = ["hero__name", "-id"]
