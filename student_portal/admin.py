from django.contrib import admin
from .models import StudentData,QuestionPaper,Marksheet
# Register your models here.



class StudentDataView(admin.ModelAdmin):
    list_display = ['studentUserModel','studentID','parentName']
    
    
admin.site.register(StudentData,StudentDataView)
admin.site.register(QuestionPaper)
admin.site.register(Marksheet)