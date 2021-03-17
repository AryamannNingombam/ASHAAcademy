from rest_framework import serializers
from .models import CarouselImage,TeacherCard



class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ['sno','name','image']

class TeacherCardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TeacherCard
        fields = ['sno','name','facultySubject','isInManagement','description',
        'qualifications','teacherImage'
        ]
