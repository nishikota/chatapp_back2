from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status
from .serializers import CustomLoginSerializer, CustomRegisterSerializer
from .models import CustomUser

# Create your views here.

