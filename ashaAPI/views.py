from .models import CarouselImage,TeacherCard,Subject
from .serializers import ContactFormSerializer, SubjectSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django import forms
from django.middleware.csrf import get_token



class ContactForm(forms.Form):
    email = forms.EmailField(label = 'Email',widget = forms.EmailInput( attrs = {'id' : 'email', 'name' : 'email','class' : 'form-control formStyle','placeholder' : 'Enter Email','required' : 'true'}))
    content = forms.CharField(label = 'Content',widget = forms.Textarea(attrs = {'id' : 'content','name' : 'content','class' : 'form-control formStyle','rows' : '10','required' : 'true' }))
    phoneNumber = forms.IntegerField(label='PhoneNumber',widget = forms.TextInput(attrs={'id' : 'phoneNumber','name' : 'phoneNumber','class' : 'form-control formStyle','placeholder' : "Enter phone number",'required' : 'true'}))
    
@api_view(['GET'])
def getToken(request):
    print(f"Get token called! :  {get_token(request)}")
    
    return JsonResponse({"success" : True,"token" : get_token(request)})


@api_view(['GET'])
def getAllCarouselImages(request):


 
        images = CarouselImage.objects.all()
        result = {
            "success" : True,
            "urls" : [],
            'totalImages' : len(images)
        }
        for image in images:
            result['urls'].append(image.image.url)
            
            

        return JsonResponse(result)
   

@api_view(['GET'])
def testRequest(request):
  
        return JsonResponse({
            "success" : True,
            "passingExam?" : False
        })



def getAllTeachersData(request):
    allTeachers = TeacherCard.objects.all()
    ser = TeacherCard(data=allTeachers,many=True)
    return Response(ser.data)


@api_view(['GET'])
def getAllTeachers(request):


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

@api_view(['POST'])
def submitContactForm(request):
    
    
        print("Submit contact called!")    
        
        ser = ContactFormSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return JsonResponse({
            'success' : True
        })
        return JsonResponse({
            'success' : False
        })



@api_view(['GET'])
def getAllSubjects(request):
    allSubjects = Subject.objects.all()
    finalResult = SubjectSerializer(data=allSubjects,many=True)
    return Response(finalResult.data)