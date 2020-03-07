from django.shortcuts import render
from portfolio.models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects' : projects})
