from default_dota_app.serializers import UpsertGuideSerializer, DetailedGuideSerializer
from default_dota_app.repositories import GuideRepository
import logging

logger = logging.getLogger(__name__)

class GuideService:
    @classmethod
    def create_guide(cls, request):
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = UpsertGuideSerializer(data=data)
        created_guide = GuideRepository.save_guide(serializer)

        if created_guide:
            logger.info(f"User {request.user} created Guide #{created_guide.id}")
            return DetailedGuideSerializer(created_guide).data

        logger.error(f"User {request.user} failed to create hero.")
