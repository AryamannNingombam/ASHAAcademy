from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class StudentData(models.Model):
    sno = models.AutoField(primary_key=True)
    studentUserModel = models.OneToOneField(User, on_delete=models.CASCADE)
    classStudyingIn = models.IntegerField(null=False, blank=False, default=8)
    studentID = models.CharField(max_length=100, blank=False, default='',unique=True)
    parentName = models.CharField(max_length=100, blank=False, default='')
    studentImage = models.ImageField(upload_to='StudentImages/',blank=True,null=True)
    parentPhoneNumber = models.IntegerField()
