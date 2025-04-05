from django.shortcuts import render
from projects.models import Project, Resume

def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:2]
    return render(request, 'pages/home.html', {'projects': featured_projects})

def about(request):
    return render(request, 'pages/about.html')

def resume(request):
    resume = Resume.objects.latest('uploaded_at')
    print("VIEW HIT ✅")
    print("PDF URL:", resume.pdf.url)
    return render(request, 'pages/resume.html', {'resume': resume})


def contact(request):
    return render(request, 'pages/contact.html')

