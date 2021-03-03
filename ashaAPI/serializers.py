from rest_framework import serializers
from .models import CarouselImage



class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ['sno','name','image']
