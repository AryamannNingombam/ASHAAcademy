from .models import CarouselImage,Subject,CVSubmission,ContactRequest
from .serializers import CVFormSerializer, ContactFormSerializer, SubjectSerializer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from django.conf import settings
from django.core.mail import send_mail



def returnFailureResponse(string1,string2):
    return {
        'success': False,
        string1: False,
        'error': string2,
    }



@api_view(['GET'])
def getToken(request):
    
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
        email = request.POST.get('email')
        ser = ContactFormSerializer(data=request.data)
        if (ser.is_valid()):
            subject = "Hello there!"
            message = "Hello! Thank you for contacting us, we will get back to you soon!"
            emailFrom = settings.EMAIL_HOST_USER
            recipientList = [email,]
            send_mail(subject,message,emailFrom,recipientList)

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

@api_view(['GET','POST'])
def signOutMainAdmin(request):
    token = request.POST.get('TOKEN')
    tempCheck = Token.objects.filter(key=token)
    if len(tempCheck) == 0:
        print("INVALIDINVALIDINVALIDINVALIDINVALIDINVALID")
        return JsonResponse(returnFailureResponse('loggedOut',"INVALID"))
    tempCheck = tempCheck[0]
    user = tempCheck.user
    if not user.is_superuser:
        return JsonResponse(returnFailureResponse('loggedOut',"NON_SUPERUSER"))
    
    return JsonResponse({
        'success': True,
        'loggedOut': True
    })








@api_view(['GET'])
def getAllCVSubmissions(request):
    token = request.headers.get('TOKEN')
    tempCheck = Token.objects.filter(key=token)
    if len(tempCheck) == 0:
        return JsonResponse(returnFailureResponse('gatAllContactRequests','Not authenticated!'))
    tempCheck  = tempCheck[0]
    user = tempCheck.user
    if not user.is_superuser:
        return JsonResponse(returnFailureResponse('gatAllContactRequests','Not authenticated!'))

    #all tests passed
    allCVSubmissions = CVSubmission.objects.all()
    finalResult = {
        'success':True,
        'allCVSubmissions' : []
    }
    for CV in allCVSubmissions:
        finalResult['allCVSubmissions'].append({
            'name' : CV.name,
'email' : CV.email,
'phoneNumber' : CV.phoneNumber,
'fileSubmission'  :CV.fileSubmission.url,
'message' : CV.message,
'subjectApplyingFor' : CV.subjectApplyingFor.name
        })
    
    return JsonResponse(finalResult)





@api_view(['GET'])
def getAllContactRequests(request):
    token = request.headers.get('TOKEN')
    tempCheck = Token.objects.filter(key=token)
    if len(tempCheck) == 0:
        return JsonResponse(returnFailureResponse('gatAllContactRequests','Not authenticated!'))
    tempCheck = tempCheck[0]
    user = tempCheck.user
    if not user.is_superuser:
        return JsonResponse(returnFailureResponse('gatAllContactRequests','Not authenticated!'))

    #all tests passed
    allContactRequests = ContactRequest.objects.all()
    finalResult = {
        'success':True,
        'allContactRequests' : []
    }
    for contactRequest in allContactRequests:
        finalResult['allContactRequests'].append({
            'name' : contactRequest.name,
'email' : contactRequest.email,
'phoneNumber' : contactRequest.phoneNumber,
'message' : contactRequest.message
        })
    
    return JsonResponse(finalResult)


@api_view(['GET','POST'])
def signInMainAdmin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    tempCheck = authenticate(username=username,password=password)
    if not  tempCheck:

        return JsonResponse(returnFailureResponse('signedIn','Invalid Credentials'))
    if not tempCheck.is_superuser:
        print("NOT SUPERUSER!")
        return JsonResponse(returnFailureResponse('signedIn',"Not authenticated"))
    print("SUPERUSER!!")
    token = Token.objects.get(user=tempCheck).key
    
    return JsonResponse({
        'success':True,
        'token':token
    })


@api_view(['GET'])
def testRequestForOnlyAdmins(request):

    token = request.headers.get('TOKEN')
    

    tempCheck = Token.objects.filter(key=token)
    if len(tempCheck) == 0:
        return JsonResponse(returnFailureResponse('accessGiven','Not authenticated'))
    tempCheck = tempCheck[0]
    user = tempCheck.user

    if not user.is_superuser:
        return JsonResponse(returnFailureResponse('accessGiven','Not enough permissions'))

    return JsonResponse({
        'success': True,
        'authenticated': True,
    })
