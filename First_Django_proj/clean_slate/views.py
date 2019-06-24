from django.shortcuts import render
from django.http import request
from .models import Sport, Mock

# Create your views here.
def main_view(request, *args, **kwargs):
    context = {
        "micovy": "Basketball",
        "atleticky": "Skok do dalky",
        # "sporty": Sport.sports.all()
    }
    return render(request, "clean_slate/main_theme.html", context)
