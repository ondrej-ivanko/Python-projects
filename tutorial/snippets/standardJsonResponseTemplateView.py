from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serialize = SnippetSerializer(snippet)
        return JsonResponse(serialize.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serialize = SnippetSerializer(snippet, data=data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize)
        return JsonResponse(serialize.errors, status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)
