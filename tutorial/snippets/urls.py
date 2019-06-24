from django.urls import path
from snippets import views, ViewSetsTemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from snippets.ModelViewsLikeURLs import *


router = DefaultRouter()
router.register(r"snippets", ViewSetsTemplateView.SnippetViewSet)
router.register(r"users", ViewSetsTemplateView.UserViewSet)


urlpatterns = [
    path('snippets/', snippet_list, name="snippet-list"),
    path('snippets/<int:pk>/', snippet_detail, name="snippet-detail"),
    path('users/',user_list, name="user-list"),
    path('users/<int:pk>/', user_detail, name="user-detail"),
    # path('', views.api_root),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name="snippet-highlight"),
]

urlpatterns = format_suffix_patterns(urlpatterns)