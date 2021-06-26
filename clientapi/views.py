from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from clientapi.models import Clients
from clientapi.serializers import ClientSerializer

# Create your views here.
@csrf_exempt
def clientApi(request, id = 0):
    if request.method == 'GET':
        clients = Clients.objects.all()
        clients_serializer = ClientSerializer(clients, many = True)
        return JsonResponse(clients_serializer.data, safe=False)