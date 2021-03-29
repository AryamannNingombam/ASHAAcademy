from django.db import models
from ashaAPI.models import Subject
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class TeacherData(models.Model):

    sno = models.AutoField(primary_key=True)
    teacherUserModel = models.OneToOneField(User,on_delete=models.CASCADE)
    teacherID = models.CharField(null=False,blank=False,max_length=100,unique=True,default='')
    facultySubject = models.ForeignKey(Subject,null=True,on_delete=models.CASCADE)
    isInManagement = models.BooleanField(default=False,blank=True)
    description = models.TextField(blank=False)
    qualifications = models.TextField(blank=False)
    teacherImage = models.ImageField(blank=False,upload_to='TeacherImages/')
    isTeacher= models.BooleanField(default=True,blank=False,null=True)
    isStudent= models.BooleanField(default=False,blank=False,null=True)

    def __str__(self):
        return self.teacherUserModel.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)



