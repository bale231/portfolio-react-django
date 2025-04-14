from django.shortcuts import render
from rest_framework import generics
from .models import Progetto
from .serializers import ProgettoSerializer

# Create your views here.

## PROGETTI
class ProgettoList(generics.ListCreateAPIView):
    queryset = Progetto.objects.all()
    serializer_class = ProgettoSerializer

class ProgettoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Progetto.objects.all()
    serializer_class = ProgettoSerializer
