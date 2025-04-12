from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

def home(request):
    return HttpResponse("<h1>Welcome to NilePS Digital System</h1>")

