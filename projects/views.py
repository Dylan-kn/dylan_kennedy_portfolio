from django.shortcuts import render, get_object_or_404
from .models import Project, Resume

def project_list(request):
    projects = Project.objects.all().order_by('ordering_index')
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    tech_stack_list = [tech.strip() for tech in project.tech_stack.split(',')]
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tech_stack_list': tech_stack_list
    })

def resume(request):
    resume = Resume.objects.latest('uploaded_at')
    print(resume.pdf.url)
    return render(request, 'pages/resume.html', {'resume': resume})
