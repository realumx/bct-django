from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("You are at about page")

def contact(request):
    return HttpResponse("You are at contact page")

def umesh(request):
    return HttpResponse("umesh")

def resume(request):
    return render(request, 'resume.html')
