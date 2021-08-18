from django.urls import path
from resume.views import home, send_message

app_name = "resume"

urlpatterns = [
    path("", home, name="home"),
    path("send-message/", send_message, name="send_message")
]
