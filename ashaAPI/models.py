from django.db import models

# Create your models here.



class CarouselImage(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,default='Carousel Image')
    image = models.ImageField(blank=False,upload_to='CarouselImages/')

    def __str__(self):
        return self.name