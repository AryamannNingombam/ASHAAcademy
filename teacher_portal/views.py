from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TeacherData
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.models import Token



@api_view(['POST'])
def signInRequest(requests):
    try:
        username = requests.POST.get('username')
        password = requests.POST.get('password')
        tempCheck = authenticate(username=username,password=password)
        if (not tempCheck):
            return JsonResponse({
                'success' : False,
                'response' : "Invalid credentials"
            })
        else:
            login(requests, tempCheck)
            token = Token.objects.get(user=tempCheck).key
            return JsonResponse({
                'logged-in': True,
                'userDetail': {
                    "username": username,
                    'password': password,
                    'token': token,
                    'teacherImage': tempCheck.teacherImage,
                    'qualifications': tempCheck.qualifications,
                    'teacherID': tempCheck.teacherID,
                    'first_name': tempCheck.teacherUserModel.first_name,
                    'last_name': tempCheck.teacherUserModel.last_name,
                    'email': tempCheck.teacherUserModel.email,
                    'facultySubject': tempCheck.facultysubject.name,
                    'isInManagement': tempCheck.isInManagement,
                    'qualifications': tempCheck.qualifications,
                    'description': tempCheck.description,
                },


            })
    except Exception as e:
        return JsonResponse({
            'logged-in': False,
            'response': e
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
            print(teacher.teacherUserModel.username)
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
        # print(finalResult)

        return JsonResponse(finalResult)



    except Exception as e:
        return JsonResponse({
        'success' : False,
        'reason' : e
    })


