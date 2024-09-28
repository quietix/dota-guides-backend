from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=200, unique=True)
    item_description = models.TextField(blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='items')

    def __str__(self):
        return f"{self.item_name}"

    class Meta:
        ordering = ["item_name"]