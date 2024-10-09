from default_dota_app.serializers import UpsertGuideSerializer, DetailedGuideSerializer
from default_dota_app.repositories import GuideRepository, UserRepository
from default_dota_app.models import Guide
from rest_framework.request import Request
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class GuideService:
    @classmethod
    def _generate_error_message(cls, message: str) -> dict:
        return {"details": message}

    @classmethod
    def get_guide(cls, request: Request, guide_id: int) -> tuple[Optional[str], Optional[dict]]:
        user = UserRepository.get_user_from_request(request)

        if UserRepository.is_user_unauthed(user):
            guide = GuideRepository.get_guide_for_unauthed_user(guide_id)
        elif UserRepository.is_user_non_admin(user):
            guide = GuideRepository.get_guide_for_non_admin_user(guide_id, user)
        elif UserRepository.is_user_admin(user):
            guide = GuideRepository.get_guide_for_admin_user(guide_id)
        else:
            logger.error(f"User identification failed. User: {user}.")
            return None, cls._generate_error_message("Something went wrong. Please, try again.")

        if guide:
            serializer = DetailedGuideSerializer(guide)
            return serializer.data, None
        else:
            return None, cls._generate_error_message("Guide is not found.")

    @classmethod
    def create_guide(cls, request: Request) -> tuple[Optional[str], Optional[dict]]:
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = UpsertGuideSerializer(data=data)
        created_guide, errors = GuideRepository.save_guide(serializer)

        if created_guide:
            return DetailedGuideSerializer(created_guide).data, None
        else:
            return None, errors

    @classmethod
    def patch_guide(cls, request: Request, guide_id: int) -> tuple[Optional[str], Optional[dict]]:
        user = UserRepository.get_user_from_request(request)

        if UserRepository.is_user_admin(user):
            guide = GuideRepository.get_guide_for_admin_user(guide_id)
        else:
            guide = GuideRepository.get_guide_for_authed_user(guide_id, user)

        if not guide:
            return None, cls._generate_error_message("Such guide doesn't exist.")

        serializer = UpsertGuideSerializer(guide, data=request.data, partial=True)
        updated_guide, errors = GuideRepository.save_guide(serializer)

        if updated_guide:
            return DetailedGuideSerializer(updated_guide).data, None
        else:
            return None, errors

    @classmethod
    def delete_guide(cls, request: Request, guide_id: int) -> tuple[Optional[bool], Optional[dict]]:
        user = UserRepository.get_user_from_request(request)

        if UserRepository.is_user_admin(user):
            guide = GuideRepository.get_guide_for_admin_user(guide_id)
        else:
            guide = GuideRepository.get_guide_for_authed_user(guide_id, user)

        is_deleted, errors = GuideRepository.delete_guide(guide)

        if is_deleted:
            return True, None
        else:
            return False, errors