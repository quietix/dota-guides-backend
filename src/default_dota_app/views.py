from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Hero
from .serializers import HeroSerializer

# Create your views here.

@api_view(['GET'])
def get_heroes(request: Request):
    heroes = Hero.objects.all()
    serializer = HeroSerializer(heroes, many=True)
    return Response(serializer.data)