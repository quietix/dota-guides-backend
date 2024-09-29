from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from default_dota_app.models import *
from default_dota_app.serializers import *


class AttributesView(APIView):
    def get(self, request):
        """
        Retrieve a list of all attributes.
        """
        attributes = Attribute.objects.all()
        serializer = AttributeSerializer(attributes, many=True)
        return Response(serializer.data)
