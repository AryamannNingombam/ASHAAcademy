from django.contrib import admin
from .models import StudentData
# Register your models here.



class StudentDataView(admin.ModelAdmin):
    list_display = ['studentUserModel','studentID','parentName']
    
    
admin.site.register(StudentData,StudentDataView)