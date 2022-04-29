from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Faculty
from .serializer import FacultyRegistrationSerializer
# Create your views here.

class FacultyRegistrationClass(generics.CreateAPIView):
    serializer_class = FacultyRegistrationSerializer
    permission_classes = [AllowAny,]
    queryset = Faculty.objects.all()
