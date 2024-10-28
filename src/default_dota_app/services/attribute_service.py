import logging

from default_dota_app.repositories import AttributeRepository, UserRepository
from default_dota_app.serializers import ReadAttributeSerializer, UpsertAttributeSerializer
from typing import Optional, Tuple
from rest_framework.request import Request
from default_dota_app.services.base_service import BaseService

logger = logging.getLogger(__name__)

class AttributeService(BaseService):
    @staticmethod
    def get_all_attributes() -> Tuple[Optional[dict], Optional[dict]]:
        attributes, errors = AttributeRepository.get_all_attributes()

        if attributes:
            serializer = ReadAttributeSerializer(attributes, many=True)
            return serializer.data, None
        else:
            return None, errors

    @staticmethod
    def get_attribute(attribute_id: int) -> Tuple[Optional[dict], Optional[dict]]:
        attribute, errors = AttributeRepository.get_attribute_by_id(attribute_id)

        if attribute:
            serializer = ReadAttributeSerializer(attribute)
            return serializer.data, None
        else:
            return None, errors

    @staticmethod
    def create_attribute(request: Request) -> Tuple[Optional[dict], Optional[dict]]:
        serializer = UpsertAttributeSerializer(data=request.data)
        created_attr, errors = AttributeRepository.save_attribute(serializer)

        if created_attr:
            return ReadAttributeSerializer(created_attr).data, None
        else:
            return None, errors

    @classmethod
    def patch_attribute(cls, request: Request, attribute_id: int) -> Tuple[Optional[dict], Optional[dict]]:
        attr, errors = AttributeRepository.get_attribute_by_id(attribute_id)

        if not attr:
            logger.error(errors)
            return None, cls._generate_error_message(f"Attribute #{attribute_id} not found.")

        serializer = UpsertAttributeSerializer(attr, data=request.data, partial=True)
        updated_attr, errors = AttributeRepository.save_attribute(serializer)

        if updated_attr:
            return ReadAttributeSerializer(updated_attr).data, None
        else:
            return None, errors

    @staticmethod
    def delete_attribute(attribute_id: int) -> Tuple[Optional[bool], Optional[dict]]:
        is_deleted, errors = AttributeRepository.delete_attribute(attribute_id)

        if is_deleted:
            return True, None
        else:
            return False, errors
