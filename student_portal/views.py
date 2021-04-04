from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import StudentData, QuestionPaper
from ashaAPI.models import Subject
from shared.requestRejectedFunction import returnRequestRejectedJson
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



@api_view(['POST'])
def signInRequest(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    tempCheck = authenticate(username=username, password=password)

    if (not tempCheck):
        return returnRequestRejectedJson()

    else:
  
        userData = StudentData.objects.get(teacherUserModel=tempCheck)
        if not userData.isStudent:
            return returnRequestRejectedJson()
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
        tempCheck = Token.objects.filter(key=token)
        if len(tempCheck) == 0:
            return returnRequestRejectedJson()
        tempCheck = tempCheck[0]
        user = tempCheck.user
        studentData = StudentData.objects.get(studentUserModel=user)
        if not studentData.isStudent:
            return returnRequestRejectedJson()

        
        return JsonResponse({
            'success': True,
            'signedOut': True,

        })

    except Exception as e:
        return returnRequestRejectedJson()





@api_view(['POST'])
def deleteStudentData(request):
    try:
        token = request.POST.get('TOKEN')
        tempCheck = Token.objects.filter(key=token)
        if len(tempCheck) == 0:
            return returnRequestRejectedJson()
        tempCheck = tempCheck[0]
        user = tempCheck.user
        if not user.is_superuser:
            return returnRequestRejectedJson()
        username = request.POST.get('username')
        studentUserToDelete = User.objects.filter(username=username)
        if len(studentUserToDelete) == 0:
            return returnRequestRejectedJson()
        
        studentUserToDelete = studentUserToDelete[0]
        studentData = StudentData.objects.get(studentUserModel=studentUserToDelete)
        if not studentData.isStudent:
            return returnRequestRejectedJson()

        studentData.delete()
        studentUserToDelete.delete()
        return JsonResponse({
            'success': True,
            'studentDeleted': True,
        })


    except Exception as e:

        return returnRequestRejectedJson()


@api_view(['POST'])
def addNewStudent(request):
    try:
        token = request.POST.get('TOKEN')
        tempCheck = Token.objects.filter(key=token)
        if len(tempCheck) ==0:
            return returnRequestRejectedJson()
        tempCheck = tempCheck[0]
        user = tempCheck.user
        if not user.is_superuser:
            return returnRequestRejectedJson()
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
        attendance = request.POST.get('attendance')


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
            attendancePercentage=attendance
        )
        newStudentData.save()

        return JsonResponse({
            'success': True,
            'studentAdded': True,
        })


    except Exception as e:
        return returnRequestRejectedJson()






@api_view(['POST'])
def updateTeacherData(request):
    try:
        token =  request.POST.get('TOKEN')
        tempCheck = Token.objects.filter(key=token)
        if len(tempCheck) == 0:
            return returnRequestRejectedJson()
        tempCheck = tempCheck[0]
        user = tempCheck.user
        if not user.is_superuser:
            return returnRequestRejectedJson()
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
        attendance = request.POST.get('attendance')
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
        newStudentData.attendancePercentage = attendance

        newStudentData.save()
        return JsonResponse({
            'success': True,
            'studentDetailsUpdated': True,
        })


    except Exception as e:
        return returnRequestRejectedJson()







@api_view(['POST'])
def uploadQuestionPaper(request):
    token = request.POST.get('TOKEN')
    tempCheck = Token.objects.filter(key=token)
    if len(tempCheck) == 0:
        return returnRequestRejectedJson()
    tempCheck = tempCheck[0]
    user = tempCheck.user
    if not user.is_superuser:
        return returnRequestRejectedJson()
    classFor = request.POST.get('classFor')
    subjectFor = Subject.objects.get(name=request.POST.get('subjectFor'))
    paperPDF = request.FILES.get('paperPDF')
    newQuestionPaper = QuestionPaper(classFor=classFor,subjectFor=subjectFor,paperPDF=paperPDF)
    newQuestionPaper.save()
    return JsonResponse({
        'success': True,
        'paperUploaded': True,
    })

