from django.shortcuts import render
from rest_framework import generics

from plant_base import models
from .serializers import PlantSerializer, BerrySerializer, FlowerSerializer, LeafSerializer, StemSerializer

class ListPlant(generics.ListCreateAPIView):
    queryset = models.Plants.objects.all()
    serializer_class = PlantSerializer

class DetailPlant(generics.RetrieveAPIView):
    queryset = models.Plants.objects.all()
    serializer_class = PlantSerializer
    lookup_field = 'name'

class ListBerry(generics.ListCreateAPIView):
    queryset = models.Berries.objects.all()
    serializer_class = BerrySerializer

class DetailBerry(generics.RetrieveAPIView):
    queryset = models.Berries.objects.all()
    serializer_class = BerrySerializer

class ListFlower(generics.ListCreateAPIView):
    queryset = models.Flowers.objects.all()
    serializer_class = FlowerSerializer

class DetailFlower(generics.RetrieveAPIView):
    queryset = models.Flowers.objects.all()
    serializer_class = FlowerSerializer

class ListLeaf(generics.ListCreateAPIView):
    queryset = models.Leaves.objects.all()
    serializer_class = LeafSerializer

class DetailLeaf(generics.RetrieveAPIView):
    queryset = models.Leaves.objects.all()
    serializer_class = LeafSerializer

class ListStem(generics.ListCreateAPIView):
    queryset = models.Stems.objects.all()
    serializer_class = StemSerializer

class DetailStem(generics.RetrieveAPIView):
    queryset = models.Stems.objects.all()
    serializer_class = StemSerializer