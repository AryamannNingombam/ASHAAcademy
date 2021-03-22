
from django.db import models

# Create your models here.

class Subject(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CarouselImage(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,default='Carousel Image')
    image = models.ImageField(blank=False,upload_to='CarouselImages/')

    def __str__(self):
        return self.name





class TeacherCard(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,default='')
    facultySubject = models.ForeignKey(Subject,null=True,on_delete=models.CASCADE)
    isInManagement = models.BooleanField(default=False,blank=True)
    description = models.TextField(blank=False)
    qualifications =  models.TextField(blank=False)
    teacherImage = models.ImageField(blank=False,upload_to='TeacherImages/')

    def __str__(self):
        return self.name
    


class ContactRequest(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,default='')
    email = models.EmailField(blank=False)
    phoneNumber = models.IntegerField(blank=False)
    message = models.TextField(blank=False,default='')


class CVSubmission(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,default='')
    email = models.EmailField(blank=False)
    phoneNumber = models.IntegerField(blank=False)
    fileSubmission = models.FileField(blank=False,upload_to='CVSubmissions/')
    message = models.TextField(blank=True,null=True,default='')
    subjectApplyingFor = models.ForeignKey(Subject,null=True,on_delete=models.CASCADE)





