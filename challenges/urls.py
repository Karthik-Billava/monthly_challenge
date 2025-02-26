from django.urls import path
from . import views

urlpatterns = [
    path("", views.index1),
    path("<int:month>/", views.monthly_challenges_int),
    path("<str:month>/", views.monthly_challenges, name="challenge-month"),
]
