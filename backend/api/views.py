from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(["GET"])
def welcome(request):
    content = {"message": "Minha primeira view em Django!"}
    return JsonResponse(content)

@api_view(["GET"])
def users(rquest):
    users = [
        {'name':'Paulo','email':'paulo@gmail.com'}
    ]

    return JsonResponse(users, safe=False)