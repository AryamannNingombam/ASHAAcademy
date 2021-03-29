from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from ashaAPI.models import Subject
from teacher_portal.models import TeacherData

class StudentData(models.Model):
    sno = models.AutoField(primary_key=True)
    studentUserModel = models.OneToOneField(User, on_delete=models.CASCADE)
    classStudyingIn = models.IntegerField(null=False, blank=False, default=8)
    studentID = models.CharField(max_length=100, blank=False, default='',unique=True)
    parentName = models.CharField(max_length=100, blank=False, default='')
    studentImage = models.ImageField(upload_to='StudentImages/',blank=True,null=True)
    parentPhoneNumber = models.IntegerField()
    isTeacher = models.BooleanField(default=False, blank=False, null=True)
    isStudent = models.BooleanField(default=True, blank=False, null=True)


def uploadToCallback(instance,filename):
    return f'StudentMarksheets/{instance.writtenBy.studentUserModel.username}/{instance.subject}/{filename}'

class Marksheet(models.Model):
    sno = models.AutoField(primary_key=True)
    writtenBy = models.ForeignKey(StudentData,on_delete=models.CASCADE)
    checkedBy = models.ForeignKey(TeacherData, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,)
    totalMarks = models.IntegerField()
    obtainedMarks = models.IntegerField()
    marksheetPDF = models.FileField(upload_to=uploadToCallback,null=False,blank=False)




@receiver(post_delete, sender=StudentData)
def submission_delete(sender, instance, **kwargs):
    instance.studentImage.delete(False)
