from default_dota_app.repositories import HeroRepository, UserRepository
from default_dota_app.serializers.hero_serializers import *
import logging

logger = logging.getLogger(__name__)

class HeroService:
    @staticmethod
    def get_hero_details(hero_id, user):
        if UserRepository.is_user_non_admin(user):
            hero = HeroRepository.get_hero_with_user_guides(hero_id, user.id)
            if hero:
                serializer = ReadHeroDetailsAsUserSerializer(hero)
        else:
            hero = HeroRepository.get_hero_with_admin_guides(hero_id)
            if hero:
                serializer = ReadHeroDetailsAsAdminSerializer(hero)

        if not hero:
            logger.error(f"Hero #{hero_id} not found.")
            return None

        logger.info(f"Retrieved and serialized details for hero #{hero_id}.")
        return serializer.data

    @staticmethod
    def patch_hero(request, hero_id):
        hero = HeroRepository.get_hero_with_admin_guides(hero_id)

        if not hero:
            logger.error(f"Hero #{hero_id} not found for update.")
            return

        serializer = UpsertHeroSerializer(hero, data=request.data, partial=True)
        hero = HeroRepository.save_hero(serializer)

        if hero:
            return ReadHeroPreviewSerializer(hero).data

        logger.error(f"Failed to update hero #{hero_id}. Saving operation failed.")

    @staticmethod
    def delete_hero(request, hero_id):
        hero = HeroRepository.get_bare_hero(hero_id)

        if hero:
            hero.delete()
            logger.info(f"User {request.user} deleted hero #{hero_id}.")
            return True

        logger.error(f"Hero #{hero_id} not found for deletion.")
        return False

    @staticmethod
    def get_hero_list(request):
        hero_name = request.GET.get('hero_name', None)
        attribute_name = request.GET.get('attribute_name', None)

        filters = {}
        if hero_name:
            filters['hero_name__icontains'] = hero_name
        if attribute_name:
            filters['attribute__attribute_name__icontains'] = attribute_name

        logger.info(f'Filtering heroes by: {filters}')

        heroes = HeroRepository.get_hero_list(**filters)
        serializer = ReadHeroPreviewSerializer(heroes, many=True)
        return serializer.data
