
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
    return render(request, 'projects/home.html', context)


# def sendEmail(request):

#     if request.method == 'POST':
#         template = render_to_string('projects/email_template.html', {
#             'name': request.POST['name'],
#             'email': request.POST['email'],
#             'subject': request.POST['subject'],
#             'message': request.POST['message'],
#         })

#         email = EmailMessage(
#             request.POST['subject'],
#             template,
#             settings.EMAIL_HOST_USER,
#             ['israelvictory87@gmail.com']
#         )

#         email.fail_silently = False
#         email.send()
#     return render(request, 'projects/email_sent.html')
