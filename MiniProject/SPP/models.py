from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Meeting(models.Model):
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f'Meeting at {self.date} {self.time}'

class Proctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    proctor_batch = models.CharField(max_length=50)


class Student(models.Model):
    name = models.CharField(max_length=100)
    college_id = models.CharField(max_length=20)
    year_of_admission = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    roll_number = models.IntegerField()
    branch = models.CharField(max_length=100)
    academic_year = models.IntegerField()  # Adjust default value
    class_name = models.CharField(max_length=100)
    semester = models.IntegerField()
    division = models.CharField(max_length=10)
    practical_batch = models.CharField(max_length=10)
    proctor_batch = models.CharField(max_length=10)
    live_kt = models.IntegerField()
    dead_kt = models.IntegerField()
    image = models.ImageField(upload_to='student_images/',null=True, blank=True)
    certificates = models.ImageField(upload_to='certificates/',null=True, blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.message}"