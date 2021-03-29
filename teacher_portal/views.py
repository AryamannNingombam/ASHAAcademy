from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import TeacherData
from ashaAPI.models import Subject
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

def returnFailureResponse(string1,string2):
    return {
        'success': False,
        string1: False,
        'error': string2,
    }








@api_view(['POST'])
def signInRequest(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
   
        
    tempCheck = authenticate(username=username,password=password)
    
    if (not tempCheck):
        return JsonResponse(returnFailureResponse('signedIn',"Invalid credentials"))
    else:
        login(request, tempCheck)
        userData = TeacherData.objects.get(teacherUserModel = tempCheck)
        token = Token.objects.get(user=tempCheck).key
        result = {
                'success': True,
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
                    'description': userData.description,
                },


            }
        return JsonResponse(result)


@api_view(['POST'])
def signOutRequest(request):
    try:
        token = request.POST.get('TOKEN')
        tempCheck = Token.objects.get(key=token)
        if not tempCheck:
            return JsonResponse(returnFailureResponse('signedOut', "INVALID_TOKEN"))
        user = tempCheck.user
        teacherData = TeacherData.objects.get(studentUserModel=user)
        if not teacherData.isTeacher:
            return JsonResponse(returnFailureResponse('signedOut', 'ONLY_STUDENTS_TO_SIGN_OUT'))

        logout(request)
        return JsonResponse({
            'success': True,
            'signedOut': True,

        })

    except Exception as e:
        return JsonResponse(returnFailureResponse('signedOut',e))


@api_view(['POST'])
def testRequest(request):
    print(request.POST)
    return JsonResponse({
        'success': True,
    })







@api_view(['GET'])
def getAllTeachers(request):
    
    try:
        finalResult = {
            'success': True,
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
        'success': False,
        'error': e
    })


@api_view(['POST'])
def deleteTeacherData(request):
    try:
        token = request.POST.get('TOKEN')
        tempCheck = Token.objects.get(key=token)
        if not tempCheck:
            return JsonResponse(returnFailureResponse('teacherDeleted',"Invalid Credentials"))
        user = tempCheck.user
        if not user.is_superuser:
            return JsonResponse(returnFailureResponse('teacherDeleted',"Not authenticated"))
        username = request.POST.get('username')
        teacherUserToDelete = User.objects.get(username=username)

        if not teacherUserToDelete:
            return JsonResponse(returnFailureResponse('teacherDeleted',"Teacher does not exist"))

        teacherData = TeacherData.objects.get(teacherUserModel=teacherUserToDelete)
        if not teacherData.isTeacher:
            return JsonResponse(returnFailureResponse('teacherDeleted',"Teacher deletion only allowed"))
        teacherData.delete()
        teacherUserToDelete.delete()
        return JsonResponse({
            'success' :True,
            'teacherDeleted' :True,
        })


    except Exception as e:

        return JsonResponse(returnFailureResponse('teacherDeleted',e))

@api_view(['POST'])
def addNewTeacher(request):
    try:
        token =  request.POST.get('TOKEN')
        tempCheck = Token.objects.get(key=token)
        if not tempCheck:
            return JsonResponse(returnFailureResponse('teacherAdded',"Invalid Credentials"))
        user = tempCheck.user
        if not user.is_superuser:
            return JsonResponse(returnFailureResponse('teacherAdded', "Not authenticated"))
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
        return JsonResponse(returnFailureResponse('teacherAdded',e))







@api_view(['POST'])
def updateTeacherData(request):
    try:
        token =  request.POST.get('TOKEN')
        tempCheck = Token.objects.get(key=token)
        if not tempCheck:
            return JsonResponse(returnFailureResponse('teacherDetailsUpdated',"Invalid Credentials"))
        user = tempCheck.user
        if not user.is_superuser:
            return JsonResponse(returnFailureResponse('teacherDetailsUpdated', "Not authenticated"))
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
        teachingSubject = Subject.objects.get(name=teacherSubject)
        user.username = username
        user.first_name = firstName
        user.last_name = lastName
        user.password = password
        user.email = email

        user.save()
        newTeacherData = TeacherData.objects.get(teacherUserModel=user)
        newTeacherData.teacherID = teacherID
        newTeacherData.isInManagement = isInManagement
        newTeacherData.teacherSubject = teacherSubject
        newTeacherData.description = description
        newTeacherData.qualifications = qualifications
        newTeacherData.teacherImage = teacherImage
        newTeacherData.teachingSubject = teachingSubject
        newTeacherData.save()
        return JsonResponse({
            'success': True,
            'teacherDetailsUpdated': True,
        })


    except Exception as e:
        return JsonResponse(returnFailureResponse('teacherDetailsUpdated',e))