from django.db import models
from default_dota_app.models.item_related.stage_model import Stage
from default_dota_app.models.item_related.item_model import Item


class ItemWrapper(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, null=True, related_name='itemwrappers')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    explanation = models.TextField(blank=True)
    order = models.SmallIntegerField(null=True)

    def __str__(self):
        return f"Item Wrapper {self.id}: {self.item}"
