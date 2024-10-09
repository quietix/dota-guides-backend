from default_dota_app.models import Guide, User
from default_dota_app.serializers import UpsertGuideSerializer
from default_dota_app.repositories.user_repository import UserRepository
from django.db.models import Q
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class GuideRepository:
    @classmethod
    def _generate_error_message(cls, message: str) -> dict:
        return {"details": message}

    @classmethod
    def get_guide_for_admin_user(cls, guide_id: int) -> Optional[Guide]:
        """
        Get guide that belongs only to admin
        """
        return Guide.objects.filter(id=guide_id).first()

    @classmethod
    def get_guide_for_non_admin_user(cls, guide_id: int, user: User) -> tuple[Optional[Guide], Optional[dict]]:
        """
        Get guide that belongs to either admin or user
        """
        if UserRepository.is_user_non_admin(user):
            admin_user = UserRepository.get_admin_user()

            if admin_user:
                return Guide.objects.filter(Q(user=user) | Q(user=admin_user), id=guide_id).first(), None
            else:
                logger.error("Failed to find admin user.")
                return None, cls._generate_error_message("Something went wrong. Try again.")

        else:
            return None, {"details": "The user cannot access this guide."}

    @classmethod
    def get_guide_for_authed_user(cls, guide_id: int, user: User) -> Optional[Guide]:
        """
        Get guide that belongs only to specified user
        """
        return Guide.objects.filter(user=user, id=guide_id).first()

    @classmethod
    def get_guide_for_unauthed_user(cls, guide_id: int) -> tuple[Optional[Guide], Optional[dict]]:
        admin_user = UserRepository.get_admin_user()

        if admin_user:
            return Guide.objects.filter(id=guide_id, user=admin_user).first(), None
        else:
            return None, cls._generate_error_message("Something went wrong. Try again.")

    @classmethod
    def save_guide(cls, serializer: UpsertGuideSerializer) -> tuple[Optional[Guide], Optional[dict]]:
        if serializer.is_valid():
            guide = serializer.save()
            return guide, None
        else:
            return None, serializer.errors

    @classmethod
    def delete_guide(cls, guide: Guide) -> tuple[Optional[bool], Optional[dict]]:
        if not guide:
            return False, cls._generate_error_message("Guide doesn't exist")

        try:
            guide.delete()
            return True, None

        except Exception as e:
            logger.error(f"Error while deleting guide: {e}")
            return False, cls._generate_error_message("Failed to delete guide.")