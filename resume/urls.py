from django.urls import path
from resume.views import home

urlpatterns = [
    path("", home, name="home"),
    # path("send-email/")
]
