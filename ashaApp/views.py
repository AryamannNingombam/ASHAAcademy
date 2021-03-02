from django.shortcuts import render

# Create your views here.




def homePage(request):
    return render(request,'ashaApp/index.html')



def faculty(request):
    return render(request,'ashaApp/faculty.html')



def contactPage(request):
    return render(request,'ashaApp/contact.html')