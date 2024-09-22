from django.db.models import Prefetch
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from default_dota_app.models import *
from default_dota_app.serializers import *


@api_view(['GET'])
def get_attributes(request: Request):
    attributes = Attribute.objects.all()
    serializer = AttributeSerializer(attributes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_heroes(request: Request):
    heroes = Hero.objects.all().prefetch_related('skills')
    serializer = HeroSerializer(heroes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_hero_details(request: Request, hero_name):
    heroes = Hero.objects.filter(hero_name=hero_name).prefetch_related('skills')
    serializer = HeroSerializer(heroes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_hero_guides(request: Request, hero_name):
    if not Hero.objects.filter(hero_name=hero_name).exists():
        return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)

    guides = Guide.objects.filter(hero__hero_name=hero_name)
    serializer = PreviewGuideSerializer(guides, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_guide_details(request: Request, guide_id):
    guides = Guide.objects.filter(id=guide_id).prefetch_related('stages__item_wrappers__item')
    serializer = DetailedGuideSerializer(guides, many=True)
    return Response(serializer.data)


# ------------------ Test ------------------ #

@api_view(['GET'])
def get_items(request: Request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_stages(request: Request):
    stages = Stage.objects.prefetch_related('item_wrappers__item').all()
    serializer = StageSerializer(stages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_guides(request: Request):
    guides = Guide.objects.prefetch_related('stages__item_wrappers__item').all()
    serializer = DetailedGuideSerializer(guides, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_skills(request: Request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_item_wrappers(request: Request):
    item_wrappers = ItemWrapper.objects.all()
    serializer = ItemWrapperSerializer(item_wrappers, many=True)
    return Response(serializer.data)
