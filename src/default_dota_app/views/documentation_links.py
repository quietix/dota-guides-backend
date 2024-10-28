from rest_framework.decorators import api_view
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    tags=["Documentation"],
    operation_summary="Get Documentation Links",
    operation_description="Fetches links to the API documentation.",
    responses={
        200: openapi.Response(
            description="Successful response with documentation links",
            examples={
                "application/json": {
                    "links": [
                        "http://example.com/api-docs",
                        "http://example.com/user-guide"
                    ]
                }
            }
        ),
        404: "Documentation links not found"
    }
)
@api_view(['GET'])
def documentation_links_view(request):
    return render(request, 'default_dota_app/documentation_links.html')
