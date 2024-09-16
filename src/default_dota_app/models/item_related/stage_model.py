from django.db import models
from default_dota_app.models.guide_model import Guide


class Stage(models.Model):
    guide = models.ForeignKey(Guide, null=True, on_delete=models.CASCADE, related_name='stages')
    stage_name = models.CharField(max_length=200)
    stage_description = models.TextField(blank=True)

    def __str__(self):
        return f"<{self.guide.hero.hero_name}> <{self.guide.guide_title}> <{self.stage_name}>"
