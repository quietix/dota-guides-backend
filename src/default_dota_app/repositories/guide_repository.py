from default_dota_app.serializers import UpsertGuideSerializer
import logging

logger = logging.getLogger(__name__)

class GuideRepository:
    @classmethod
    def save_guide(cls, serializer: UpsertGuideSerializer):
        if serializer.is_valid():
            guide = serializer.save()
            return guide
        logger.error(f"Failed to create Guide. Errors: {serializer.errors}")