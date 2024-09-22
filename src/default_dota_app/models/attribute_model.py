from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Max


def get_next_display_order():
    max_order = Attribute.objects.aggregate(Max('display_order'))['display_order__max']
    return (max_order + 1) if max_order is not None else 1


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=30)
    img = models.ImageField(null=True, blank=True, upload_to='attributes')
    display_order = models.IntegerField(
        default=get_next_display_order,
        validators=[
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return f"{self.attribute_name}"

    class Meta:
        ordering = ['display_order']
