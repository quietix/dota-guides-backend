from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from default_dota_app.services import AttributeService
from rest_framework import status
from knox.auth import TokenAuthentication
import logging
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

logger = logging.getLogger(__name__)

class AttributeListView(APIView):
    def get_authenticators(self):
        if self.request.method == 'GET':
            return []
        elif self.request.method == 'POST':
            return [TokenAuthentication()]
        else:
            return super().get_authenticators()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAdminUser()]

    @swagger_auto_schema(
        tags=["Attributes"],
        operation_summary="Retrieve all attributes",
        operation_description="Get a list of all attributes.",
        responses={
            200: openapi.Response("Successful Response"),
            400: openapi.Response("Bad Request")
        }
    )
    def get(self, request):
        attributes_data, errors = AttributeService.get_all_attributes()

        if attributes_data:
            return Response(attributes_data, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["Attributes"],
        operation_summary="Create a new attribute",
        operation_description="Create a new attribute with the provided details.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the attribute'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the attribute'),
            },
        ),
        responses={
            201: openapi.Response("Attribute created successfully", schema=openapi.Schema(type=openapi.TYPE_OBJECT)),
            400: "Bad Request"
        }
    )
    def post(self, request):
        created_attribute_data, errors = AttributeService.create_attribute(request)

        if created_attribute_data:
            return Response(created_attribute_data, status=status.HTTP_201_CREATED)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
