from django.db import models
from django.core.validators import MinValueValidator


class ItemSection(models.Model):
    section_name = models.CharField(max_length=200, unique=True)
    img = models.ImageField(null=True, blank=True, upload_to='item_sections')
    display_order = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return f"<{self.section_name}> <#{self.id}>"
