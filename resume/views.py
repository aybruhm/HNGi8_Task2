
from django.shortcuts import render, redirect
from .models import Project, User

# Email Configuration
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage


def home(request):
    projects = Project.objects.all()
    user = User.objects.all()
    context = {
        'projects': projects,
        'user': user,
    }
    return render(request, 'resume/index.html', context)


def send_message(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")

    print(name)
    print(email)
    print(subject)
    print(message)
    return redirect("resume:home")
