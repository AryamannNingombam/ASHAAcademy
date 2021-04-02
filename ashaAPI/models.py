
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

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


class ContactRequest(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,default='')
    email = models.EmailField(blank=False)
    phoneNumber = models.IntegerField(blank=False)
    message = models.TextField(blank=False,default='')

    def __str__(self):
        return f'{self.name} | {self.email}'





class CVSubmission(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,default='')
    email = models.EmailField(blank=False)
    phoneNumber = models.IntegerField(blank=False)
    fileSubmission = models.FileField(blank=False,upload_to='CVSubmissions/')
    message = models.TextField(blank=True,null=True,default='')
    subjectApplyingFor = models.ForeignKey(Subject,blank=False,null=False,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.email}'

#code to delete images/files when a model instance is deleted

@receiver(post_delete, sender=CarouselImage)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(post_delete, sender=CVSubmission)
def submission_delete(sender, instance, **kwargs):
    instance.fileSubmission.delete(False)


