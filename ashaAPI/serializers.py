from rest_framework import serializers
from .models import CarouselImage, ContactRequest,TeacherCard,Subject



class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ['sno','name','image']


class ContactFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactRequest
        fields = [
            'name','email','phoneNumber','message'
        ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject 
        fields = [
            'name'
        ]