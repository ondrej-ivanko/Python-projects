"""First_Django_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from pages.views import homepage_view, new_page_view, simple_view, if_stat
from tutorial.views import describe_user
from clean_slate.views import main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage_view, name='home'),
    path('new/', new_page_view, name='home'),
    path('about/', simple_view, name='home'),
    path('if/', if_stat, name="home"),
    path("detailed/", describe_user),
    path("sports/", include("clean_slate.urls")),
]
