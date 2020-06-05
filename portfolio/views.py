from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse("Mario's Portfolio.")


def contact(request):
    return HttpResponse("Message Me.")