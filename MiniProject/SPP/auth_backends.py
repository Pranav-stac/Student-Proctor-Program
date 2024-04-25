  
from django.contrib.auth.backends import ModelBackend

class NoLastLoginModelBackend(ModelBackend):
         def update_last_login(self, request, user):
             pass  # Do nothing to prevent updating last_login

     # auth_backends.py
from django.contrib.auth.backends import BaseBackend
from .models import Student

class CustomStudentAuthBackend(BaseBackend):
         def authenticate(self, request, college_id=None, roll_number=None):
             try:
                 student = Student.objects.get(college_id=college_id, roll_number=roll_number)
                 return student  # Assuming Student model does not have a OneToOneField to User
             except Student.DoesNotExist:
                 return None         