from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("helloworld")
    
def about(request):
    return HttpResponse("aboutdata")

def contact(request):
    return HttpResponse("contactdata")