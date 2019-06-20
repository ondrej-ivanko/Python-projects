from django.shortcuts import render

from .models import User
# Create your views here.
def describe_user(request):
    obj = User.objects.get(id=1)
    content = {
        "age": obj.age,
        "name": obj.name
    }
    return render(request, "user/detailed.html", content)

#Další způsob psaní:
def dalsi_describe_user(request):
    obj = User.objects.get(id=1)
    content = {
        "user": obj
    }
    return render(request, "user/detailed.html", content)
