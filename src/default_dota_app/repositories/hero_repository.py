from django.db.models import Prefetch
from default_dota_app.models import Hero, Guide
from default_dota_app.repositories.user_repository import UserRepository
from default_dota_app.serializers.hero_serializers import UpsertHeroSerializer


class HeroRepository:
    @staticmethod
    def get_hero_with_admin_guides(hero_id, admin_username="admin"):
        admin_user = UserRepository.get_admin_user(admin_username)
        admin_guides = Guide.objects.filter(user=admin_user)
        prefetch_admin_guides = Prefetch('guides', queryset=admin_guides)
        return Hero.objects.filter(id=hero_id).prefetch_related('skills', prefetch_admin_guides).first()

    @staticmethod
    def get_hero_with_user_guides(hero_id, user_id, admin_username="admin"):
        authed_user = UserRepository.get_non_admin_user_by_id(user_id)
        authed_user_guides = Guide.objects.filter(user=authed_user)

        admin_user = UserRepository.get_admin_user(admin_username)
        admin_guides = Guide.objects.filter(user=admin_user)

        prefetch_user_guides = Prefetch('guides', queryset=authed_user_guides, to_attr='user_guides')
        prefetch_admin_guides = Prefetch('guides', queryset=admin_guides, to_attr='admin_guides')

        return Hero.objects.filter(id=hero_id).prefetch_related('skills', prefetch_user_guides, prefetch_admin_guides).first()

    @staticmethod
    def save_hero(serializer: UpsertHeroSerializer):
        if serializer.is_valid():
            return serializer.save()

    @staticmethod
    def get_bare_hero(hero_id):
        return Hero.objects.filter(id=hero_id).first()

    @staticmethod
    def get_hero_list(**kwargs):
        if kwargs:
            return Hero.objects.filter(**kwargs)
        return Hero.objects.all()
