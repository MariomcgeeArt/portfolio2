from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse("Portfolio Home.")
    #returns Home page with Marios Profile


def contact(request):
    return HttpResponse("Contact Me.")
    #returne page with text Contact  Me


def greet_by_name(request, name):
    return HttpResponse("<h1> Welcome, {} !</h1>".format(name))
  # Return an HttpResponse that contains a string that includes the given name

