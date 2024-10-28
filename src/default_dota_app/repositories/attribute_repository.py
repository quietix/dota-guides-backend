from default_dota_app.repositories.base_repository import BaseRepository
from default_dota_app.models import Attribute
from default_dota_app.serializers.attribute_serializers.upsert_attribute_serializer import UpsertAttributeSerializer
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
    @BaseRepository.handle_repository_exceptions("Attribute not found.")
    def get_attribute_by_id(attr_id: int) -> Tuple[Optional[Attribute], Optional[str]]:
        return Attribute.objects.get(id=attr_id), None

    @staticmethod
    @BaseRepository.handle_repository_exceptions("Error filtering attributes.")
    def filter_attributes(attr_name: str) -> Tuple[Optional[QuerySet[Attribute]], Optional[str]]:
        return Attribute.objects.filter(attribute_name__icontains=attr_name), None

    @staticmethod
    @BaseRepository.handle_repository_exceptions("Error saving attribute.")
    def save_attribute(serializer: UpsertAttributeSerializer) -> Tuple[Optional[Attribute], Optional[dict]]:
        if serializer.is_valid():
            new_attr = serializer.save()
            return new_attr, None
        else:
            return None, serializer.errors

    @staticmethod
    @BaseRepository.handle_repository_exceptions("Error deleting attribute.")
    def delete_attribute(id: int) -> Tuple[Optional[bool], Optional[str]]:
        deleted_count, _ = Attribute.objects.filter(id=id).delete()
        if deleted_count > 0:
            return True, None
        else:
            return False, "No such attribute found."
