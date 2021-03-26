from django.db import models
from ashaAPI.models import Subject
from django.contrib.auth.models import User



class TeacherData(models.Model):
    sno = models.AutoField(primary_key=True)
    teacherUserModel = models.OneToOneField(User,on_delete=models.CASCADE)
    teacherID = models.CharField(null=False,blank=False,max_length=100,unique=True,default='')
    facultySubject = models.ForeignKey(Subject,null=True,on_delete=models.CASCADE)
    isInManagement = models.BooleanField(default=False,blank=True)
    description = models.TextField(blank=False)
    qualifications = models.TextField(blank=False)
    teacherImage = models.ImageField(blank=False,upload_to='TeacherImages/')

    def __str__(self):
        return self.teacherUserModel.username



