from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TeacherData


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


