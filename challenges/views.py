from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenge = {
    "january": "Do yoga atleast for 10 minutes",
    "february": "Do not eat junk food for entire month",
    "march": "Do exercise atleast for 20 minutes day in this entire month",
    "april": "Learn Django atleast for 30 minutes a day",
    "may": "walk for 30 minutes",
    "june": "cycling for 30 minutes",
    "july": "learn web dev for 1 hour",
    "agust": "learn swimming",
    "september": "learn dsa in c++",
    "october": "practice spirituality",
    "november": "read any self-development book for 1hr",
    "december": None
}


def monthly_challenges_int(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("<h2 color='red'>Invalid month</h2>")
    redirect_month = months[month-1]
    redirect_path = reverse("challenge-month", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported yet!")
