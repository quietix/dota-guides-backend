from rest_framework.response import Response
from rest_framework import views as drf_views
from rest_framework.permissions import IsAdminUser
from default_dota_app.models import *
from default_dota_app.serializers.user_serializers import *
from drf_yasg.utils import swagger_auto_schema


class GetAllUsersView(drf_views.APIView):
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(
        tags=["Admin Actions: Users"],
        operation_summary="Get All Users",
        operation_description="Get All Users",
    )
    def get(self, request):
        users = User.objects.all()
        serializer = ReadUserSerializer(users, many=True)
        return Response(serializer.data)
