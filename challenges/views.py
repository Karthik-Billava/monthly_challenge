from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request):
    return HttpResponse("Exercise for 30 minutes daily")

def february(request):
    return HttpResponse("No junk food")