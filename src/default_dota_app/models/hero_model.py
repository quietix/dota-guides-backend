from django.db import models


class Hero(models.Model):
    STRENGTH = "STRENGTH"
    AGILITY = "AGILITY"
    INTELLIGENCE = "INTELLIGENCE"
    UNIVERSAL = "UNIVERSAL"

    ATTRIBUTE_CHOICES = {
        STRENGTH: 'Strength',
        AGILITY: 'Agility',
        INTELLIGENCE: 'Intelligence',
        UNIVERSAL: 'Universal',
    }

    hero_name = models.CharField(max_length=200)
    attribute = models.CharField(
        max_length=20,
        choices=ATTRIBUTE_CHOICES,
        default=UNIVERSAL)
    img = models.ImageField(null=True, blank=True, upload_to='heroes')


    def __str__(self):
        return f"{self.hero_name}"

    class Meta:
        ordering = ["hero_name"]
