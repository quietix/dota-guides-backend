from default_dota_app.serializers import UpsertGuideSerializer, DetailedGuideSerializer
from default_dota_app.repositories import GuideRepository, UserRepository
from default_dota_app.models import Guide
from rest_framework.request import Request
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class GuideService:
    @classmethod
    def get_guide(cls, request: Request, guide_id: int) -> Optional[Guide]:
        user = UserRepository.get_user_from_request(request)

        if UserRepository.is_user_unauthed(user):
            guide = GuideRepository.get_guide_for_unauthed_user(guide_id)
        elif UserRepository.is_user_non_admin(user):
            guide = GuideRepository.get_guide_for_non_admin_user(guide_id, user)
        elif UserRepository.is_user_admin(user):
            guide = GuideRepository.get_guide_for_admin_user(guide_id)
        else:
            logger.error(f"User identification failed. User: {user}")
            return None

        if guide:
            serializer = DetailedGuideSerializer(guide)
            return serializer.data

        logger.warning(f"Guide #{guide_id} for User {user} is not found.")
        return None

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
