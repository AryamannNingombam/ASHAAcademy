from django.urls import path
from . import views


urlpatterns = [
    path("sign-in-student/",views.signInRequest,name='signInRequest'),
    path('student-change-password/',views.changePassword,name="student-change-password")
]