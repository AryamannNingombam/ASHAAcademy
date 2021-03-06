from django.shortcuts import render
from .models import CarouselImage
from .serializers import CarouselImageSerializer
from django.http import JsonResponse

def getAllCarouselImages(request):
    if (request.method == 'GET'):
        images = CarouselImage.objects.all()
        result = ""
        for image in images:

            result += image.image.url +','
            
            

        return JsonResponse({
            "success" : True,
            "urls" : str(result[:len(result)-1])
        })
    return JsonResponse({
        "success" : False
    })


def testRequest(request):
    if (request.method == 'GET'):
        return JsonResponse({
            "success" : True,
            "passingExam?" : False
        })
    return JsonResponse({
        "success" : True,
        'passingExam?' : False
    })