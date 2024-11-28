from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import views as drf_views
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging
from default_dota_app.services import GuideService

logger = logging.getLogger(__name__)

class CreateGuideView(drf_views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Guides"],
        operation_summary="Create a Guide",
        operation_description="Create a new guide for the authenticated user.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['hero', 'guide_title'],
            properties={
                'hero': openapi.Schema(type=openapi.TYPE_STRING, description='Name of hero'),
                'display_order': openapi.Schema(type=openapi.TYPE_INTEGER, description='Order of the guide display'),
                'guide_title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the guide'),
                'guide_description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the guide')
            }
        )
    )
    def post(self, request):
        create_guide_data = GuideService.create_guide(request)

        if create_guide_data:
            return Response(create_guide_data, status=status.HTTP_201_CREATED)

        return Response({"detail": "Create hero failed."}, status=status.HTTP_400_BAD_REQUEST)
