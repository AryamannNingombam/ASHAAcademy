from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import TeacherData
from ashaAPI.models import Subject
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@api_view(['POST'])
def signInRequest(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
   
        
    tempCheck = authenticate(username=username,password=password)
    
    if (not tempCheck):
        return JsonResponse({
                'success' : False,
                'response' : "Invalid credentials"
            })
    else:
        login(request, tempCheck)
        userData = TeacherData.objects.get(teacherUserModel = tempCheck)
        token = Token.objects.get(user=tempCheck).key
        result ={
                'logged-in': True,
                'userDetail': {
                    "username": username,
                    'token': token,
                    'teacherImage': userData.teacherImage.url,
                    'qualifications': userData.qualifications,
                    'teacherID': userData.teacherID,
                    'first_name': userData.teacherUserModel.first_name,
                    'last_name': userData.teacherUserModel.last_name,
                    'email': userData.teacherUserModel.email,
                    'facultySubject': userData.facultySubject.name,
                    'isInManagement': userData.isInManagement,
                    'qualifications': userData.qualifications,
                    'description': userData.description,
                },


            }
        print(result)
        return JsonResponse(result)

        



@api_view(['POST'])
def testRequest(request):
    print(request.POST)
    return JsonResponse({
        'success' :True,
    })



@api_view(['GET'])
def getAllTeachers(request):
    
    try:
        finalResult = {
            'success' : True,
            'teachersList' : []

        }
        allTeachersDB = TeacherData.objects.all()
        for teacher in allTeachersDB:

            finalResult['teachersList'].append({
                'firstName' : teacher.teacherUserModel.first_name,
                'lastName' : teacher.teacherUserModel.last_name,
                'email' : teacher.teacherUserModel.email,
                'description' : teacher.description,
                'teacherImage' : teacher.teacherImage.url,
                'qualifications' : teacher.qualifications,
                'isInManagement' : teacher.isInManagement,
                'facultySubject' : teacher.facultySubject.name


            })


        return JsonResponse(finalResult)



    except Exception as e:
        return JsonResponse({
        'success' : False,
        'reason' : e
    })



@api_view(['POST'])
def addNewTeacher(request):
    try:
        token =  request.POST.get('TOKEN')
        tempCheck = Token.objects.get(key=token)
        if not tempCheck:
            return JsonResponse({
                'success' : False,
                'error' : "Invalid Credentials"
            })
        user = tempCheck.user
        if not user.is_superuser:
            return JsonResponse({
                'success' : False,
                'error' : "Not authenticated"
            })
        username = request.POST.get('username')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        password = request.POST.get('password')
        email = request.POST.get('email')
        teacherID = request.POST.get('teacherID')
        isInManagement = request.POST.get('isInManagement')
        teacherSubject = request.POST.get('teacherSubjects')
        description = request.POST.get('description')
        qualifications=  request.POST.get('qualifications')
        teacherImage = request.FILES.get('teacherImage')
        newUser = User.objects.create_user(
            username=username,
            password=password,email=email,is_active=True,
            first_name=firstName,last_name=lastName,
            is_superuser=False,

        )
        teachingSubject = Subject.objects.get(name=teacherSubject)

        newUser.save()
        newTeacherData = TeacherData(
        teacherUserModel=newUser,
        teacherID=teacherID,
        isInManagement=isInManagement,
        description=description,
        facultySubject=teachingSubject,
        qualifications=qualifications,
        teacherImage=teacherImage
        )
        newTeacherData.save()

        return JsonResponse({
            'success': True,
            'teacherAdded': True,
        })


    except Exception as e:
        return JsonResponse({
            'success' : False,
            'error' : e,
        })