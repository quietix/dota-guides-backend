from rest_framework import status
from rest_framework.response import Response
from rest_framework import views as drf_views
from rest_framework.permissions import IsAuthenticated
from default_dota_app.serializers import *
from drf_yasg.utils import swagger_auto_schema
import logging
from default_dota_app.services import GuideService
from drf_yasg import openapi


logger = logging.getLogger(__name__)

class GuideDetailsView(drf_views.APIView):
    @swagger_auto_schema(
        tags=["Guides"],
        operation_summary="Retrieve Guide Details",
        operation_description="Retrieve a guide by its ID for the authenticated user or the admin."
    )
    def get(self, request, id):
        guide_data, errors = GuideService.get_guide(request, id)

        if guide_data:
            return Response(guide_data, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["Guides"],
        operation_summary="Update an Existing Guide",
        operation_description="Update an existing guide by its ID for the authenticated user.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'hero': openapi.Schema(type=openapi.TYPE_STRING, description='Name of hero'),
                'display_order': openapi.Schema(type=openapi.TYPE_INTEGER, description='Order of the guide display'),
                'guide_title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the guide'),
                'guide_description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the guide')
            }
        )
    )
    def patch(self, request, id):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        updated_guide_data, errors = GuideService.patch_guide(request, id)

        if updated_guide_data:
            return Response(updated_guide_data, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["Guides"],
        operation_summary="Delete a Guide",
        operation_description="Delete a guide by its ID for the authenticated user."
    )
    def delete(self, request, id):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        is_deleted, errors = GuideService.delete_guide(request, id)

        if is_deleted:
            return Response({"detail": "Guide successfully deleted."}, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
