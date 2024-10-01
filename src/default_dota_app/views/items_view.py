from django.contrib.auth.models import User
from django.db.models import Prefetch
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from default_dota_app.models import *
from default_dota_app.serializers import *


class ItemsView(APIView):
    def get(self, request):
        item_sections = ItemSection.objects.all().prefetch_related('items')
        serializer = ItemSectionSerializer(item_sections, many=True)
        return Response(serializer.data)
