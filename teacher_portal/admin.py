from django.contrib import admin
from .models import TeacherData
# Register your models here.



class TeacherDataView(admin.ModelAdmin):
    list_display =  ['teacherID','facultySubject']


admin.site.register(TeacherData,TeacherDataView)