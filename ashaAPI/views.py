from .models import CarouselImage,Subject,CVSubmission
from .serializers import CVFormSerializer, ContactFormSerializer, SubjectSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token


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




@api_view(['POST'])
def submitContactForm(request):
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
    finalResult = {
        'success' : True,
        'subjects' : []
    }
    for subject in allSubjects:
        finalResult['subjects'].append(subject.name)
    return JsonResponse(finalResult)

@api_view(['POST'])
def postCVForm(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNumber =request.POST.get('phoneNumber')
        fileSubmission = request.FILES.get('fileSubmission')
        message = request.POST.get('message')
        print(request.POST.get('subjectApplyingFor'))
        subjectApplyingFor = Subject.objects.get(name=request.POST.get('subjectApplyingFor'))
        print(subjectApplyingFor)
        newCVSubmission = CVSubmission(name=name,email=email,phoneNumber=phoneNumber,fileSubmission=fileSubmission,message=message,subjectApplyingFor=subjectApplyingFor)
        newCVSubmission.save()
        return JsonResponse({
         'success' : True,
     })  
    except Exception as e:
        return JsonResponse({
            'success' : False,
            'error' : e
        })

    