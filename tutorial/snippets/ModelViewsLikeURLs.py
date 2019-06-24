from snippets.ViewSetsTemplateView import SnippetViewSet, UserViewSet

from rest_framework import renderers

# Tenhle template slouží jako ukázka jak se dělají ModelViews

snippet_list = SnippetViewSet.as_view({
    "get": "list",
    "post": "create"
})

snippet_detail = SnippetViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "patrial_update",
    "delete": "destroy",
})

snippet_highlight = SnippetViewSet.as_view({
    "get": "highlight"
}, renderer_classes=[renderers.StaticHTMLRenderer]
)

user_list = UserViewSet.as_view({
    "get": "list",
})

user_detail = UserViewSet.as_view({
    "get": "retrieve"
})


