from django.shortcuts import render
from rest_framework import generics, serializers
from servicioCliente.models import Soporte, PQR
from servicioCliente.serializer import PQRSerializer, SoporteSerializer

# Create your views here.


class SoporteListCreate(generics.ListCreateAPIView):
    queryset = Soporte.objects.all()
    serializers_class= SoporteSerializer


class SoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soporte.objects.all()
    serializers_class= SoporteSerializer

class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializers_class= PQRSerializer 

class PQRpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQR.objects.all()
    serializers_class= PQRSerializer 