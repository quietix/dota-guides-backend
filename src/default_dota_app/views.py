from django.db.models import Prefetch
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from default_dota_app.models import *
from default_dota_app.serializers import *

@api_view(['GET'])
def get_attributes(request: Request):
    """
    Retrieve a list of all attributes.

    **Response:**
    - 200 OK: A list of attributes with their details.
    - Example response:
    ```json
    [
        {
            "id": 1,
            "attributeName": "Universal",
            "img": "https://example.com/path/to/image.png"
        },
        ...
    ]
    ```
    """
    attributes = Attribute.objects.all()
    serializer = AttributeSerializer(attributes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_heroes(request: Request):
    """
    Retrieve a list of all heroes with their skills.

    **Response:**
    - 200 OK: A list of heroes with their details and associated skills.
    - Example response:
    ```json
    [
        {
            "id": 2,
            "heroName": "Abaddon",
            "img": "https://example.com/path/to/image.png",
            "skills": []
        },
        ...
    ]
    ```
    """
    heroes = Hero.objects.all().prefetch_related('skills')
    serializer = HeroSerializer(heroes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_hero_details(request: Request, hero_name):
    """
    Retrieve details of a specific hero by name.

    **Parameters:**
    - hero_name: The name of the hero.

    **Response:**
    - 200 OK: Hero details including skills.
    - 404 Not Found: If the hero does not exist.
    - Example response:
    ```json
    {
        "id": 2,
        "heroName": "Abaddon",
        "img": "https://example.com/path/to/image.png",
        "skills": []
    }
    ```
    """
    heroes = Hero.objects.filter(hero_name=hero_name).prefetch_related('skills')
    if not heroes.exists():
        return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = HeroSerializer(heroes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_hero_guides(request: Request, hero_name):
    """
    Retrieve guides for a specific hero by name.

    **Parameters:**
    - hero_name: The name of the hero.

    **Response:**
    - 200 OK: A list of guides related to the specified hero.
    - 404 Not Found: If the hero does not exist.
    - Example response:
    ```json
    [
        {
            "id": 2,
            "guideTitle": "Hard lane (3-d position)"
        },
        ...
    ]
    ```
    """
    if not Hero.objects.filter(hero_name=hero_name).exists():
        return Response({"detail": "Hero not found."}, status=status.HTTP_404_NOT_FOUND)

    guides = Guide.objects.filter(hero__hero_name=hero_name)
    serializer = PreviewGuideSerializer(guides, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_guide_details(request: Request, guide_id):
    """
    Retrieve details of a specific guide by ID.

    **Parameters:**
    - guide_id: The ID of the guide.

    **Response:**
    - 200 OK: Guide details, including stages and item wrappers.
    - 404 Not Found: If the guide does not exist.
    - Example response:
    ```json
    {
        "id": 2,
        "guideTitle": "Hard lane (3-d position)",
        "stages": [
            {
                "id": 4,
                "stageName": "Early game",
                "itemWrappers": [...]
            },
            ...
        ]
    }
    ```
    """
    guides = Guide.objects.filter(id=guide_id).prefetch_related('stages__item_wrappers__item')
    if not guides.exists():
        return Response({"detail": "Guide not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = DetailedGuideSerializer(guides, many=True)
    return Response(serializer.data)

# ------------------ Test ------------------ #

@api_view(['GET'])
def get_items(request: Request):
    """
    Retrieve a list of all items.

    **Response:**
    - 200 OK: A list of items with their details.
    - Example response:
    ```json
    [
        {
            "id": 1,
            "itemName": "Clarity",
            "itemDescription": "Restores mana.",
            "img": "https://example.com/path/to/image.png"
        },
        ...
    ]
    ```
    """
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_stages(request: Request):
    """
    Retrieve a list of all stages with their item wrappers.

    **Response:**
    - 200 OK: A list of stages with their details and associated item wrappers.
    - Example response:
    ```json
    [
        {
            "id": 4,
            "stageName": "Early game",
            "itemWrappers": [...]
        },
        ...
    ]
    ```
    """
    stages = Stage.objects.prefetch_related('item_wrappers__item').all()
    serializer = StageSerializer(stages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_guides(request: Request):
    """
    Retrieve a list of all guides.

    **Response:**
    - 200 OK: A list of guides with their details.
    - Example response:
    ```json
    [
        {
            "id": 2,
            "guideTitle": "Hard lane (3-d position)",
            "stages": [...]
        },
        ...
    ]
    ```
    """
    guides = Guide.objects.prefetch_related('stages__item_wrappers__item').all()
    serializer = DetailedGuideSerializer(guides, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_skills(request: Request):
    """
    Retrieve a list of all skills.

    **Response:**
    - 200 OK: A list of skills with their details.
    - Example response:
    ```json
    [
        {
            "id": 1,
            "skillName": "Berserker's Call",
            "skillDescription": "Axe taunts nearby enemy units.",
            "img": "https://example.com/path/to/image.png"
        },
        ...
    ]
    ```
    """
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_item_wrappers(request: Request):
    """
    Retrieve a list of all item wrappers.

    **Response:**
    - 200 OK: A list of item wrappers with their associated items.
    - Example response:
    ```json
    [
        {
            "id": 3,
            "item": {
                "id": 6,
                "itemName": "Clarity",
                "itemDescription": "Restores mana.",
                "img": "https://example.com/path/to/image.png"
            },
            "itemWrapperExplanation": ""
        },
        ...
    ]
    ```
    """
    item_wrappers = ItemWrapper.objects.all()
    serializer = ItemWrapperSerializer(item_wrappers, many=True)
    return Response(serializer.data)
