from rest_framework.response import Response
from rest_framework.views import APIView
from default_dota_app.services import AttributeService
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status


class AttributeDetailsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        attribute_data, errors = AttributeService.get_attribute(id)

        if attribute_data:
            return Response(attribute_data, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        updated_attribute_data, errors = AttributeService.patch_attribute(request, id)

        if updated_attribute_data:
            return Response(updated_attribute_data, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)

        is_deleted, errors = AttributeService.delete_attribute(id)

        if is_deleted:
            return Response({"detail": "Guide successfully deleted."}, status=status.HTTP_200_OK)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
