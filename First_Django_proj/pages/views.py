from django.shortcuts import render
from django.http import HttpResponse, request


# Create your views here.
def homepage_view(*args, **kwargs):
    return HttpResponse("<p>Yeah it´s working</p>")

def new_page_view(request, *args, **kwargs):
    return render(request, "template.html", {})

def simple_view(request, *args, **kwargs):
    my_context = {
        "name": "stuff",
        "time": 123,
        "serial": [45, 89, 74]
        }
    return render(request, "about.html", my_context)

def if_stat(request, *args, **kwargs):
    top = {
        "choices": [1, 2, 8, 9]
    }
    return render(request, "ifstatements.html", top)
