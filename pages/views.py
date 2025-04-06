from django.shortcuts import render, redirect
from .forms import ContactForm
from projects.models import Project, Resume
from django.contrib import messages
from .models import ContactMessage

def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:2]
    return render(request, 'pages/home.html', {'projects': featured_projects})

def about(request):
    return render(request, 'pages/about.html')

def resume_view(request):
    print("Incoming Host:", request.get_host())
    resume = Resume.objects.latest('uploaded_at')
    return render(request, 'pages/resume.html', {'resume': resume})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Thank you for your message. I will get back to you shortly.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})

