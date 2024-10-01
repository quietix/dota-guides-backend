from django.db import models
from default_dota_app.models.item_related.item_section import ItemSection


class Item(models.Model):
    item_section = models.ForeignKey(ItemSection, default=1, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=200, unique=True)
    item_description = models.TextField(blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='items')

    def __str__(self):
        return f"{self.item_name}"

    class Meta:
        ordering = ["item_name"]