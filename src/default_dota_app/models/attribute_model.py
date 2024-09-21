from django.db import models


class Attribute(models.Model):
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

    attribute_name = models.CharField(
        max_length=20,
        choices=ATTRIBUTE_CHOICES,
        default=UNIVERSAL)

    img = models.ImageField(null=True, blank=True, upload_to='attributes')

    def __str__(self):
        return f"{self.attribute_name}"
