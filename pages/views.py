from django.shortcuts import render
from projects.models import Project

def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:2]
    return render(request, 'pages/home.html', {'projects': featured_projects})

def about(request):
    return render(request, 'pages/about.html')

def resume(request):
    return render(request, 'pages/resume.html')

def contact(request):
    return render(request, 'pages/contact.html')

