from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenges_int(request, month):
    return HttpResponse(month)


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Exercise for 30 minutes daily"
    elif month == "february":
        challenge_text = "No junk food"
    elif month == "march":
        challenge_text = "Meditate for 30 minutes"
    else:
        return HttpResponseNotFound("This month is not supported yet!")
    return HttpResponse(challenge_text)
