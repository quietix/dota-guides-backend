from django.db import models
from default_dota_app.models.guide_model import Guide
from default_dota_app.models.talent_related.talent_model import Talent


class TalentWrapper(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True, related_name='talentwrappers')
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, null=True)
    explanation = models.TextField(blank=True)

    def __str__(self):
        if self.guide:
            return f"Talent Wrapper {self.id} of Guide {self.guide.id}: {self.talent}"
        else:
            return f"Talent Wrapper {self.id} (No Guide)"
