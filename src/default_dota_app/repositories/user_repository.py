from default_dota_app.models import User


class UserRepository:
    @staticmethod
    def get_admin_user(admin_username="admin"):
        return User.objects.filter(is_superuser=True, username=admin_username).first()

    @staticmethod
    def get_non_admin_user_by_id(user_id):
        return User.objects.filter(is_superuser=False, id=user_id).first()

    @staticmethod
    def is_user_non_admin(user):
        return user.is_authenticated and not user.is_superuser
