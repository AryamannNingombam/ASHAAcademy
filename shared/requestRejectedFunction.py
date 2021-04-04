from django.http import JsonResponse

def returnRequestRejectedJson():
    return JsonResponse({
        'success':False,
        'message' : "Not authenticated"
    })