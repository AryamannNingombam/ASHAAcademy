
from django.db import models

# Create your models here.



class CarouselImage(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,default='Carousel Image')
    image = models.ImageField(blank=False,upload_to='CarouselImages/')

    def __str__(self):
        return self.name




class TeacherCard(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,default='')
    facultySubject = models.CharField(max_length=50,blank=True,default='')
    isInManagement = models.BooleanField(default=False,blank=True)
    description = models.TextField(blank=False)
    qualifications =  models.TextField(blank=False)

    def __str__(self):
        return self.name
    

class TeacherImage(models.Model):
    sno = models.AutoField(primary_key=True)
    teacher = models.OneToOneField(TeacherCard,on_delete=models.CASCADE)
    image = models.ImageField(blank=False,upload_to='TeacherImages/')


    def __str__(self):
        return self.teacher.name
