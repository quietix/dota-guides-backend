from django.core.validators import MinValueValidator
from django.db import models


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=30, unique=True)
    img = models.ImageField(null=True, blank=True, upload_to='attributes')
    display_order = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return f"{self.attribute_name}"

    class Meta:
        ordering = ['display_order']
