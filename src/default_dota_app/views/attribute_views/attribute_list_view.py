from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from default_dota_app.services import AttributeService
from rest_framework import status
from knox.auth import TokenAuthentication
import logging

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

    def get(self, request):
        attributes_data, errors = AttributeService.get_all_attributes()

        if attributes_data:
            return Response(attributes_data, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        created_attribute_data, errors = AttributeService.create_attribute(request)

        if created_attribute_data:
            return Response(created_attribute_data, status=status.HTTP_201_CREATED)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
