from default_dota_app.repositories.base_repository import BaseRepository
from default_dota_app.models import Attribute
from typing import Optional, Tuple
from django.db.models import QuerySet
import logging

logger = logging.getLogger(__name__)

class AttributeRepository(BaseRepository):
    @staticmethod
    @BaseRepository.handle_repository_exceptions("Error fetching attributes.")
    def get_all_attributes() -> Tuple[QuerySet[Attribute], Optional[str]]:
        return Attribute.objects.all(), None

    @staticmethod
    @BaseRepository.handle_repository_exceptions("Error fetching attribute.")
    def get_attribute_by_id(attr_id: int) -> Tuple[Optional[Attribute], Optional[str]]:
        return Attribute.objects.get(id=attr_id), None

    @staticmethod
    @BaseRepository.handle_repository_exceptions("Error filtering attributes.")
    def filter_attributes(attr_name: str) -> Tuple[Optional[QuerySet[Attribute]], Optional[str]]:
        return Attribute.objects.filter(attribute_name__icontains=attr_name), None

    @staticmethod
    @BaseRepository.handle_repository_exceptions("Error adding attribute.")
    def add_attribute(attribute_name: str, img=None, display_order=None) -> Tuple[Optional[Attribute], Optional[str]]:
        if not attribute_name:
            return None, "Attribute name cannot be empty."

        display_order = 1 if display_order is None else display_order
        new_attr = Attribute(attribute_name=attribute_name, img=img, display_order=display_order)
        new_attr.save()
        return new_attr, None

    @staticmethod
    @BaseRepository.handle_repository_exceptions("Error deleting attribute.")
    def delete_attribute(id: int) -> Tuple[Optional[bool], Optional[str]]:
        deleted_count, _ = Attribute.objects.filter(id=id).delete()
        if deleted_count > 0:
            return True, None
        else:
            return False, "No such attribute found."
