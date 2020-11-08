from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, from Home")

def profile(request):
    return HttpResponse("HI I AM FROM PROFILE")    

    