from django.db.models import Prefetch
from default_dota_app.models import Hero, Guide, User


class HeroRepository:
    @staticmethod
    def get_hero_with_admin_guides(hero_id, admin_username="admin"):
        admin_user = User.objects.get(is_superuser=True, username=admin_username)
        admin_guides = Guide.objects.filter(user=admin_user)
        prefetch_admin_guides = Prefetch('guides', queryset=admin_guides)
        return Hero.objects.filter(id=hero_id).prefetch_related('skills', prefetch_admin_guides).first()

    @staticmethod
    def get_hero_with_user_guides(hero_id, user_id):
        authed_user = User.objects.get(id=user_id, is_superuser=False)
        authed_user_guides = Guide.objects.filter(user=authed_user)

        admin_user = User.objects.get(is_superuser=True, username="admin")
        admin_guides = Guide.objects.filter(user=admin_user)

        prefetch_user_guides = Prefetch('guides', queryset=authed_user_guides, to_attr='user_guides')
        prefetch_admin_guides = Prefetch('guides', queryset=admin_guides, to_attr='admin_guides')

        return Hero.objects.filter(id=hero_id).prefetch_related('skills', prefetch_user_guides, prefetch_admin_guides).first()