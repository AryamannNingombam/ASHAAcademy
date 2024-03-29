"""ASHAAcademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('getCarouselImages/',views.getAllCarouselImages,name='all_images'),
   path('testApi/',views.testRequest,name = 'test'),
    path("postContactForm/",views.submitContactForm,name='postContactForm'),
    path('getCSRFToken/',views.getToken,name='getCSRFToken'),
    path('getAllSubjects/',views.getAllSubjects,name='getAllSubjects'),
    path('postCVForm/',views.postCVForm,name='postCVForm'),
    path('signInMainAdmin/',views.signInMainAdmin,name='signInMainAdmin'),
    path('signOutMainAdmin/', views.signOutMainAdmin,name='signOutMainAdmin'),
    path('testApiForOnlyAdmins/',views.testRequestForOnlyAdmins,name='testRequestForOnlyAdmins'),
    path('getAllContactRequests/',views.getAllContactRequests,name='getAllContactRequests'),
    path('getAllCVSubmissions/',views.getAllCVSubmissions,name='getAllCVSubmissions'),
    path('getAllNotifications/',views.getAllNotifications,name='getAllNotifications'),
    path('postNewNotification/',views.addNotification,name='postNewNotification')

]