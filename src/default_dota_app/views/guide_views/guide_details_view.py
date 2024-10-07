from rest_framework import status
from rest_framework.response import Response
from rest_framework import views as drf_views
from rest_framework.permissions import IsAuthenticated
from default_dota_app.models import *
from default_dota_app.serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging
from default_dota_app.services import GuideService


logger = logging.getLogger(__name__)

class GuideDetailsView(drf_views.APIView):
    @swagger_auto_schema(
        tags=["Guides"],
        operation_summary="Retrieve Guide Details",
        operation_description="Retrieve a guide by its ID for the authenticated user or the admin.",
        responses={
            200: openapi.Response('Successful retrieval of guide details', DetailedGuideSerializer),
            404: openapi.Response('Guide not found for this user.'),
        }
    )
    def get(self, request, id):
        guide_data = GuideService.get_guide(request, id)

        if guide_data:
            return Response(guide_data, status=status.HTTP_200_OK)

        return Response({"detail": f"Guide #{id} not found."}, status=status.HTTP_404_NOT_FOUND)

    # TODO patch, delete
    @swagger_auto_schema(
        tags=["Guides"],
        operation_summary="Update an Existing Guide",
        operation_description="Update an existing guide by its ID for the authenticated user.",
        request_body=UpsertGuideSerializer,
        responses={
            200: openapi.Response('Successful update of the guide', UpsertGuideSerializer),
            400: openapi.Response('Invalid input data'),
            404: openapi.Response('Guide not found for this user.'),
        }
    )
    def patch(self, request, id):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        user = request.user

        try:
            guide = Guide.objects.get(user=user, id=id)
            serializer = UpsertGuideSerializer(guide, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                logger.info(f"User {user} has updated Guide #{id}")
                return Response(serializer.data, status=status.HTTP_200_OK)

            logger.error(f"User {user} has failed to update Guide #{id}. Errors: {serializer.errors}.")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Guide.DoesNotExist:
            logger.error(f"User {user} has failed to update Guide #{id}. Guide #{id} does not exist.")
            return Response({"detail": "Guide with such ID is not found for this user."},
                            status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        tags=["Guides"],
        operation_summary="Delete a Guide",
        operation_description="Delete a guide by its ID for the authenticated user.",
        responses={
            204: openapi.Response('Guide successfully deleted.'),
            404: openapi.Response('Guide not found for this user.'),
        }
    )
    def delete(self, request, id):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        user = request.user

        try:
            guide = Guide.objects.get(user=user, id=id)
            guide.delete()
            return Response({"detail": "Guide successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Guide.DoesNotExist:
            return Response({"detail": "Guide with such ID is not found for this user."},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": e}, status=status.HTTP_400_BAD_REQUEST)