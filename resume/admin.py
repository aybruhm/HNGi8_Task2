from django.contrib import admin
from resume.models import User, Project, Tag, Message


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Message)
