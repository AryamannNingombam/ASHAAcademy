from django.urls import path
from . import views


urlpatterns = [
    path('getAllTeachers/',views.getAllTeachers,name='getAllTeachers'),
    path("sign-in-teacher/",views.signInRequest,name='signInTeacher')
]