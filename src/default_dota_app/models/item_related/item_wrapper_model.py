from django.db import models

from default_dota_app.models.item_related.item_model import Item
from default_dota_app.models.item_related.stage_model import Stage


class ItemWrapper(models.Model):
    stage = models.ForeignKey(Stage, null=True, on_delete=models.CASCADE, related_name='item_wrappers')
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
    item_wrapper_explanation = models.TextField(blank=True)

    def __str__(self):
        return f"<{self.stage.guide.hero.hero_name}> <{self.stage.guide.guide_title}> <{self.stage.stage_name}> <Wrapper {self.item.item_name}> #{self.id}"
