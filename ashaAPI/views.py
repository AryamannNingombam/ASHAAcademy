from django.shortcuts import render
from .models import CarouselImage
from .serializers import CarouselImageSerializer
from django.http import JsonResponse
from django import forms




class ContactForm(forms.Form):
    email = forms.EmailField(label = 'Email',widget = forms.EmailInput( attrs = {'id' : 'email', 'name' : 'email','class' : 'form-control formStyle','placeholder' : 'Enter Email','required' : 'true'}))
    content = forms.CharField(label = 'Content',widget = forms.Textarea(attrs = {'id' : 'content','name' : 'content','class' : 'form-control formStyle','rows' : '10','required' : 'true' }))
    phoneNumber = forms.IntegerField(label='PhoneNumber',widget = forms.TextInput(attrs={'id' : 'phoneNumber','name' : 'phoneNumber','class' : 'form-control formStyle','placeholder' : "Enter phone number",'required' : 'true'}))
    
    
    



def getAllCarouselImages(request):
    if (request.method == 'GET'):
        images = CarouselImage.objects.all()
        result = ""
        for image in images:

            result += image.image.url +','
            
            

        return JsonResponse({
            "success" : True,
            "urls" : str(result[:len(result)-1])
        })
    return JsonResponse({
        "success" : False
    })


def testRequest(request):
    if (request.method == 'GET'):
        return JsonResponse({
            "success" : True,
            "passingExam?" : False
        })
    return JsonResponse({
        "success" : True,
        'passingExam?' : False
    })