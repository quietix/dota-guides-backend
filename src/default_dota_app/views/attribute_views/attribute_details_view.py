from rest_framework.response import Response
from rest_framework.views import APIView
from default_dota_app.services import AttributeService
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class AttributeDetailsView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=["Attributes"],
        operation_summary="Get attribute details by ID",
        operation_description="Retrieve the details of a specific attribute using its ID.",
        responses={
            200: openapi.Response("Successful Response", schema=openapi.Schema(type=openapi.TYPE_OBJECT)),
            400: "Bad Request"
        }
    )
    def get(self, request, id):
        attribute_data, errors = AttributeService.get_attribute(id)

        if attribute_data:
            return Response(attribute_data, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["Attributes"],
        operation_summary="Update attribute by ID",
        operation_description="Update the details of a specific attribute using its ID.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the attribute'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the attribute'),
                # Add more fields as necessary
            },
        ),
        responses={
            200: openapi.Response("Successful Response", schema=openapi.Schema(type=openapi.TYPE_OBJECT)),
            400: "Bad Request"
        }
    )
    def patch(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        updated_attribute_data, errors = AttributeService.patch_attribute(request, id)

        if updated_attribute_data:
            return Response(updated_attribute_data, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["Attributes"],
        operation_summary="Delete attribute by ID",
        operation_description="Delete a specific attribute using its ID.",
        responses={
            200: openapi.Response("Successful Response", schema=openapi.Schema(type=openapi.TYPE_OBJECT)),
            400: "Bad Request"
        }
    )
    def delete(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        is_deleted, errors = AttributeService.delete_attribute(id)

        if is_deleted:
            return Response({"detail": "Guide successfully deleted."}, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
