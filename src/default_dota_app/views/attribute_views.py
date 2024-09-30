from rest_framework.response import Response
from rest_framework.views import APIView

from default_dota_app.models import *
from default_dota_app.serializers import *


class AttributesView(APIView):
    def get(self, request):
        attributes = Attribute.objects.all()
        serializer = AttributeSerializer(attributes, many=True)
        return Response(serializer.data)
