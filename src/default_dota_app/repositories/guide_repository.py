from default_dota_app.models import Guide, User
from default_dota_app.serializers import UpsertGuideSerializer
from default_dota_app.repositories.user_repository import UserRepository
from django.db.models import Q
from typing import Optional


class GuideRepository:
    @classmethod
    def get_guide_for_admin_user(cls, guide_id: int) -> Optional[Guide]:
        return Guide.objects.filter(id=guide_id).first()

    @classmethod
    def get_guide_for_non_admin_user(cls, guide_id: int, user: User) -> Optional[Guide]:
        is_non_admin_user = UserRepository.is_user_non_admin(user)

        if is_non_admin_user:
            admin_user = UserRepository.get_admin_user()

            if admin_user:
                return Guide.objects.filter(Q(user=user) | Q(user=admin_user), id=guide_id).first()

        return None

    @classmethod
    def get_guide_for_unauthed_user(cls, guide_id):
        admin_user = UserRepository.get_admin_user()

        if admin_user:
            return Guide.objects.filter(id=guide_id, user=admin_user).first()

        return None

    @classmethod
    def save_guide(cls, serializer: UpsertGuideSerializer):
        if serializer.is_valid():
            guide = serializer.save()
            return guide

        return None
