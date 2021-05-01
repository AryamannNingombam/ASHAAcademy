from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import StudentData, QuestionPaper,Marksheet
from ashaAPI.models import Subject
from shared.requestRejectedFunction import returnRequestRejectedJson
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from teacher_portal.models import TeacherData


@api_view(['POST'])
def signInRequest(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
   
    tempCheck =  authenticate(username=username, password=password)
    
    if (not tempCheck):
        return returnRequestRejectedJson()

    else:
        try:
            userData = StudentData.objects.get(studentUserModel=tempCheck)
     
            if not userData.isStudent:
                return returnRequestRejectedJson()
            token = Token.objects.get(user=tempCheck).key
            
            result = {
                'success': True,
                'role' : "STUDENT",
                   'token': token,
                'userDetail': {
                    'username': username,
                 
                    'firstName': userData.studentUserModel.first_name,
                    'lastName': userData.studentUserModel.last_name,
                    'email': userData.studentUserModel.email,
                    'classStudyingIn': userData.classStudyingIn,
                    'studentID': userData.studentID,
                    'parentName': userData.parentName,
                    'studentImage': userData.studentImage.url,
                    'parentPhoneNumber': userData.parentPhoneNumber


                }

            }
            return JsonResponse(result)
        except Exception as e:
            print(e)
            return returnRequestRejectedJson()


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


@api_view(['GET'])
def getAllQuestionPapers(request):
    try:
        token = request.headers.token
        tempCheck = Token.objects.filter(key=token)
        if not tempCheck:
            return returnRequestRejectedJson()
        finalResult = {
        'success':True,
        'allQuestionPapers' : []
        }
        allQuestionPapers = QuestionPaper.objects.all()
        for questionPaper in allQuestionPapers:
            finalResult['allQuestionPapers'].append({
            
            'classFor' : questionPaper.classFor,
            'paperPDF' : questionPaper.paperPDF.url,
            "subjectFor" : questionPaper.subjectFor.name
            })

        return JsonResponse(finalResult)
        
    except Exception as e:
        return returnRequestRejectedJson()
        



@api_view(['GET'])
def getAllMarksheets(request):
    token = request.headers.token
    tempCheck = Token.objects.filter(key=token)
    if not tempCheck:
        return returnRequestRejectedJson()
    student = StudentData.objects.filter(studentUserModel=tempCheck.user)
    if len(student) == 0:
        return returnRequestRejectedJson()
    student = student[0]
    allMarksheets = Marksheet.objects.filter(writtenBy=student)
    finalResult = {
    'success':True,
    'allMarksheets' : []
    }
    for marksheet in allMarksheets:
        finalResult['allMarksheets'].append({


        'checkedBy' : marksheet.checkedBy.teacherUserModel.username ,
        'subject' : marksheet.subject.name ,
        'totalMarks' : marksheet.totalMarks ,
        'obtainedMarks' : marksheet.obtainedMarks ,


        'marksheetPDF' : marksheet.marksheetPDF.url ,
        'questionPaper' : marksheet.questionPaper.paperPDF.url ,
        })
    return JsonResponse(finalResult)


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


@api_view(['POST'])
def changePassword(request):
    try:
        token = request.POST.get('TOKEN')
        oldPassword = request.POST.get('oldPassoword')
        newPassword = request.POST.get('newPassword')

        testAuth = Token.objects.get(key=token)
        if not testAuth:
            return returnRequestRejectedJson()
        userData = testAuth.user
        if (userData.password == oldPassword):
            print("Updating the password!")
            userData.password = newPassword
            userData.save()
            return JsonResponse({'success':True,
            userData : userData,
            token:token
            })

        else:
            return returnRequestRejectedJson()

    except Exception as e:
        print("Exception!")
        return returnRequestRejectedJson()




@api_view(['POST'])
def uploadMarksheet(request):
    try:
            token = request.POST.get('TOKEN')
            tempCheck = Token.objects.filter(key=token)
            if len(tempCheck) == 0:
                return returnRequestRejectedJson()
            tempCheck = tempCheck[0]
            teacher = tempCheck.user
            studentToken = request.POST.get('studentToken')
            if not studentToken:
                return returnRequestRejectedJson()
            tempCheck = Token.objects.filter(studentToken)
            if len(tempCheck) == 0:
                return returnRequestRejectedJson()
            tempCheck = tempCheck[0]
            student = StudentData.objects.get(studentUserModel=tempCheck.user)
            subjectName = request.POST.get('subject')
            newMarksheet = Marksheet(writtenBy=student,
            checkedBy=TeacherData.objects.get(teacherUserModel=teacher),
            subject = Subject.objects.get(name=subjectName),
                totalMarks=request.POST.get('totalMarks'),
                obtainedMarks=request.POST.get('obtainedMarks'),
                marksheetPDF=request.FILES.get('marksheetPDF'),
            questionPaper=QuestionPaper.objects.get(sno=request.POST.get('questionPaperSNO')
            ))

            newMarksheet.save()
            return JsonResponse({
                'success': True,
                'marksheetUploaded': True,
            })     
    except Exception as e:
        return returnRequestRejectedJson()