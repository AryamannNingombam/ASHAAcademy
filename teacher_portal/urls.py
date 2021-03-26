from django.urls import path
from . import views


urlpatterns = [
    path('getAllTeachers/',views.getAllTeachers,name='getAllTeachers')
]