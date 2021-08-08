from rest_framework import serializers
from plant_base import models

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'name',
        'latin_name',
        'isNative',
        'image_name'
        )
        model= models.Plants

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'plant',
        'image_name',
        'colors',
        'desc'
        )
        model= models.Flowers
        
class BerrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'plant',
        'image_name',
        'colors',
        'desc'
        )
        model= models.Berries

class LeafSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'plant',
        'image_name',
        'shapes',
        'desc'
        )
        model= models.Leaves
        
class StemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'plant',
        'desc'
        )
        model= models.Stems