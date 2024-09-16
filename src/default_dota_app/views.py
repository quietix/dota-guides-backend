from django.db.models import Prefetch
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from default_dota_app.models import *
from default_dota_app.serializers import *

@api_view(['GET'])
def get_heroes(request: Request):
    heroes = Hero.objects.all()
    serializer = HeroSerializer(heroes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_hero(request: Request, hero_name):
    heroes = Hero.objects.filter(hero_name=hero_name)
    serializer = HeroSerializer(heroes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_stages(request: Request):
    stages = Stage.objects.all()
    serializer = StageSerializer(stages, many=True)
    # item_wrappers = ItemWrapper.objects.all()
    # serializer = ItemWrapperSerializer(item_wrappers, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def get_guides(request: Request, hero_name):
#     guides = Guide.objects.filter(hero__hero_name=hero_name)
#
#     guides = Guide.objects.prefetch_related(
#         Prefetch('stages', queryset=Stage.objects.prefetch_related('itemwrappers')),
#         Prefetch('skillbuilds', queryset=SkillBuild.objects.all()),
#         Prefetch('talentwrappers', queryset=TalentWrapper.objects.all())
#     )
#     serializer = GuideSerializer(guides, many=True)
#     return Response(serializer.data)