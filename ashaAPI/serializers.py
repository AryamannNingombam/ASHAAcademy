from rest_framework import serializers
from .models import CVSubmission, CarouselImage, ContactRequest,Subject



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


class CVFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = CVSubmission
        fields = [
            'name',
'email',
'phoneNumber',
'fileSubmission',
'message',
'subjectApplyingFor',
        ]