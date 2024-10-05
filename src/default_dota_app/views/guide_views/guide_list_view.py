from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import views as drf_views
from default_dota_app.models import *
from default_dota_app.serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging


logger = logging.getLogger(__name__)

class CreateGuideView(drf_views.APIView):
    @swagger_auto_schema(
        tags=["Guides"],
        operation_summary="Create a Guide",
        operation_description="Create a new guide for the authenticated user.",
        request_body=UpsertGuideSerializer,
        responses={
            201: openapi.Response(
                description='Guide created successfully',
                schema=DetailedGuideSerializer,
            ),
            400: openapi.Response(description='Invalid input data'),
            403: openapi.Response(description='Forbidden (user not authenticated)'),
        }
    )
    def post(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        serializer = UpsertGuideSerializer(data=request.data)

        if serializer.is_valid():
            guide = serializer.save()
            logger.info(f"Created Guide #{guide.id}")
            return Response(DetailedGuideSerializer(guide).data, status=status.HTTP_201_CREATED)

        logger.error(f"User {request.user} failed to create Guide. Errors: {serializer.errors}.")
        return Response(f"User {request.user} failed to create Guide. Errors: {serializer.errors}.",
                        status=status.HTTP_400_BAD_REQUEST)
