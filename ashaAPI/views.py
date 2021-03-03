from django.shortcuts import render
from .models import CarouselImage
from .serializers import CarouselImageSerializer
from django.http import JsonResponse

def getAllCarouselImages(request,sno):
    if (request.method == 'GET'):
        image = CarouselImage.objects.get(sno=sno)
        # ser = CarouselImageSerializer(image,many=True)
        return JsonResponse({
            "success" : True,
            "url" : image.image.url
        })
    return JsonResponse({
        "success" : False
    })
