from default_dota_app.repositories import HeroRepository
from default_dota_app.serializers import ReadHeroDetailsAsAdminSerializer, ReadHeroDetailsAsUserSerializer
import logging

logger = logging.getLogger(__name__)


class HeroService:
    @staticmethod
    def get_hero_details(hero_id, user):
        if user.is_authenticated and not user.is_superuser:
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
