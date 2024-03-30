# admin.py

from django.contrib import admin
from .models import Announcement, Meeting, Student, Proctor, Message

admin.site.register(Announcement)
admin.site.register(Meeting)
admin.site.register(Student)
admin.site.register(Proctor)
admin.site.register(Message)
