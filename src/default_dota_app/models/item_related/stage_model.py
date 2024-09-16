from django.db import models
from default_dota_app.models.guide_model import Guide


class Stage(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True, related_name='stages')
    stage_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        if self.guide:
            return f"Stage {self.id} of Guide {self.guide.id}"
        else:
            return f"Stage {self.id} (No Guide)"