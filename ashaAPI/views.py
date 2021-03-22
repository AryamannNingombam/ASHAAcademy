from django.shortcuts import render
from .models import CarouselImage,TeacherCard
from .serializers import TeacherCardSerializer,ContactFormSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from django import forms



class ContactForm(forms.Form):
    email = forms.EmailField(label = 'Email',widget = forms.EmailInput( attrs = {'id' : 'email', 'name' : 'email','class' : 'form-control formStyle','placeholder' : 'Enter Email','required' : 'true'}))
    content = forms.CharField(label = 'Content',widget = forms.Textarea(attrs = {'id' : 'content','name' : 'content','class' : 'form-control formStyle','rows' : '10','required' : 'true' }))
    phoneNumber = forms.IntegerField(label='PhoneNumber',widget = forms.TextInput(attrs={'id' : 'phoneNumber','name' : 'phoneNumber','class' : 'form-control formStyle','placeholder' : "Enter phone number",'required' : 'true'}))
    
    
    



def getAllCarouselImages(request):
    if (request.method == 'GET'):
        images = CarouselImage.objects.all()
        result = {
            "success" : True,
            "urls" : [],
            'totalImages' : len(images)
        }
        for image in images:
            result['urls'].append(image.image.url)
            
            

        return JsonResponse(result)
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


def getAllTeachersData(request):
    allTeachers = TeacherCard.objects.all()
    ser = TeacherCard(data=allTeachers,many=True)
    return Response(ser.data)



def getAllTeachers(request):
    if (request.method == 'GET'):
        allTeachers = TeacherCard.objects.all()
        finalResult = {'success' : True,'numberOfTeachers' : len(allTeachers),'teachersList' : []}
       
        for teacher in allTeachers:
            finalResult['teachersList'].append({
            'name' : teacher.name,
            'facultySubject': teacher.facultySubject.name,
'isInManagement': teacher.isInManagement,
'description':teacher.description,
'qualifications':teacher.qualifications,
'teacherImage':teacher.teacherImage.url
        }) 
      
        return JsonResponse(finalResult)


def submitContactForm(request):
    if (request.method == 'POST'):
        
        ser = ContactFormSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
        return JsonResponse({
            'success' : True
        })

    return JsonResponse({
        'success' : False
    })