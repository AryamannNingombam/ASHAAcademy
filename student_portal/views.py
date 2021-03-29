from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import StudentData
from ashaAPI.models import Subject
from django.contrib.auth import login, logout, authenticate
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

    tempCheck = authenticate(username=username, password=password)

    if (not tempCheck):
        return JsonResponse(returnFailureResponse('signedIn', "Invalid credentials"))

    else:
        login(request, tempCheck)
        userData = StudentData.objects.get(teacherUserModel=tempCheck)
        if not userData.isStudent:
            return JsonResponse(returnFailureResponse('signedIn', "Student only portal"))
        token = Token.objects.get(user=tempCheck).key
        result = {
            'success': True,
            'userDetail': {
                'username': username,
                'token': token,
                'firstName': userData.studentUserModel.first_name,
                'lastName': userData.studentUserModel.last_name,
                'email': userData.studentUserModel.email,
                'classStudyingIn': userData.classStudyingIn,
                'studentID': userData.studentID,
                'parentName': userData.parentName,
                'studentImage': userData.studentImage,
                'parentPhoneNumber': userData.parentPhoneNumber


            }

        }
        return JsonResponse(result)


@api_view(['POST'])
def signOutRequest(request):

    
    try:
        token = request.POST.get('TOKEN')
        tempCheck = Token.objects.get(key=token)
        if not tempCheck:
            return JsonResponse(returnFailureResponse('signedOut',"INVALID_TOKEN"))
        user = tempCheck.user
        studentData = StudentData.objects.get(studentUserModel=user)
        if not studentData.isStudent:
            return JsonResponse(returnFailureResponse('signedOut','ONLY_STUDENTS_TO_SIGN_OUT'))

        logout(request)
        return JsonResponse({
            'success': True,
            'signedOut': True,

        })

    except Exception as e:
        return JsonResponse(returnFailureResponse(e))





@api_view(['POST'])
def deleteStudentData(request):
    try:
        token = request.POST.get('TOKEN')
        tempCheck = Token.objects.get(key=token)
        if not tempCheck:
            return JsonResponse(returnFailureResponse('studentDeleted', "Invalid Credentials"))
        user = tempCheck.user
        if not user.is_superuser:
            return JsonResponse(returnFailureResponse('studentDeleted', "Not authenticated"))
        username = request.POST.get('username')
        studentUserToDelete = User.objects.get(username=username)
        if not studentUserToDelete:
            return JsonResponse(returnFailureResponse('studentDeleted', "Student does not exist"))
        
        
        studentData = StudentData.objects.get(studentUserModel=studentUserToDelete)
        if not studentData.isStudent:
            return JsonResponse(returnFailureResponse('studentDeleted', 'Student deletion only allowed'))

        studentData.delete()
        studentUserToDelete.delete()
        return JsonResponse({
            'success': True,
            'studentDeleted': True,
        })


    except Exception as e:

        return JsonResponse(returnFailureResponse('studentDeleted',e))


@api_view(['POST'])
def addNewStudent(request):
    try:
        token = request.POST.get('TOKEN')
        tempCheck = Token.objects.get(key=token)
        if not tempCheck:
            return JsonResponse(returnFailureResponse('studentAdded', "Invalid Credentials"))
        user = tempCheck.user
        if not user.is_superuser:
            return JsonResponse(returnFailureResponse('studentAdded',  "Not authenticated"))
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        classStudyingIn = request.POST.get('classStudyingIn')
        studentID = request.POST.get('studentID')
        parentName = request.POST.get('parentName')
        studentImage = request.FILES.get('studentImage')
        parentPhoneNumber = request.POST.get('parentPhoneNumber')


        newUser = User.objects.create_user(
            username=username,
            password=password, email=email, is_active=True,
            first_name=firstName, last_name=lastName,
            is_superuser=False,

        )


        newUser.save()
        newStudentData = StudentData(
        studentUserModel = newUser,
        classStudyingIn = classStudyingIn,
        studentID = studentID,
        parentName = parentName,
        studentImage = studentImage,
        parentPhoneNumber = parentPhoneNumber,
        )
        newStudentData.save()

        return JsonResponse({
            'success': True,
            'studentAdded': True,
        })


    except Exception as e:
        return JsonResponse(returnFailureResponse('studentAdded', "Not authenticated"))






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
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        classStudyingIn = request.POST.get('classStudyingIn')
        studentID = request.POST.get('studentID')
        parentName = request.POST.get('parentName')
        studentImage = request.FILES.get('studentImage')
        parentPhoneNumber = request.POST.get('parentPhoneNumber')
        user.username = username
        user.first_name = firstName
        user.last_name = lastName
        user.password = password
        user.email = email






        user.save()
        newStudentData = StudentData.objects.get(studentUserModel=user)
        newStudentData.classStudyingIn = classStudyingIn
        newStudentData.studentID = studentID
        newStudentData.parentName = parentName
        newStudentData.studentImage = studentImage
        newStudentData.parentPhoneNumber = parentPhoneNumber


        newStudentData.save()
        return JsonResponse({
            'success': True,
            'studentDetailsUpdated': True,
        })


    except Exception as e:
        return JsonResponse(returnFailureResponse('studentDetailsUpdated',e))