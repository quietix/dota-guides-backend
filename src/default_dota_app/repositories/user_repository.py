from default_dota_app.models import User
from rest_framework.request import Request
from typing import Optional


class UserRepository:
    @staticmethod
    def get_admin_user(admin_username:str = "admin") -> Optional[User]:
        return User.objects.filter(is_superuser=True, username=admin_username).first()

    @staticmethod
    def get_non_admin_user_by_id(user_id: int) -> Optional[User]:
        return User.objects.filter(is_superuser=False, id=user_id).first()

    @staticmethod
    def get_user_from_request(request: Request) -> Optional[User]:
        return request.user

    @staticmethod
    def is_user_admin(user: User) -> bool:
        return user.is_superuser

    @staticmethod
    def is_user_non_admin(user: User) -> bool:
        return user.is_authenticated and not user.is_superuser

    @staticmethod
    def is_user_unauthed(user: User) -> bool:
        return not user.is_authenticated

    @staticmethod
    def is_user_authed(user: User) -> bool:
        return user.is_authenticated

    @classmethod
    def is_user_authed(cls, request: Request) -> bool:
        user = cls.get_user_from_request(request)
        return user.is_authenticated
