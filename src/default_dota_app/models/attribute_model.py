from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Max


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=30)
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

    def save(self, *args, **kwargs):
        if not self.pk:  # If this is a new object
            max_order = Attribute.objects.aggregate(Max('display_order'))['display_order__max'] or 0
            self.display_order = max_order + 1
        super().save(*args, **kwargs)

    @classmethod
    def reorder(cls):
        for index, obj in enumerate(cls.objects.order_by('display_order'), start=1):
            obj.display_order = index
            obj.save()
