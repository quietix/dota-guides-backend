from rest_framework.decorators import api_view
from django.shortcuts import render


@api_view(['GET'])
def documentation_links_view(request):
    return render(request, 'default_dota_app/documentation_links.html')
