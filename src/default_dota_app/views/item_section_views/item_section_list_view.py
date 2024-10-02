from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from default_dota_app.models import *
from default_dota_app.serializers import *
from drf_yasg.utils import swagger_auto_schema
import logging


logger = logging.getLogger(__name__)

class ItemSectionListView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=["Item Section"],
        operation_description="Retrieve all item sections",
        responses={200: ReadItemSectionSerializer(many=True)}
    )
    def get(self, request):
        logger.info("Getting all Item Sections")
        item_sections = ItemSection.objects.all()
        serializer = ReadItemSectionSerializer(item_sections, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        tags=["Item Section"],
        operation_description="Create a new item section (Admin only)",
        request_body=UpsertItemSectionSerializer,
        responses={
            201: ReadItemSectionSerializer,
            400: 'Invalid input'
        }
    )
    def post(self, request):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        serializer = UpsertItemSectionSerializer(data=request.data)

        if serializer.is_valid():
            item_section = serializer.save()
            logger.info(f"Created Item Section #{item_section.id}")
            return Response(ReadItemSectionSerializer(item_section).data, status=status.HTTP_201_CREATED)

        logger.error(f"User {request.user.username} failed to create an Item Section. Errors: {serializer.errors}.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
