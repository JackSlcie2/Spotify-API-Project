from django.shortcuts import render
from rest_framework import generics
from .serializers import PSerializer
from .models import Pacientes

class PacientesView(generics.CreateAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PSerializer