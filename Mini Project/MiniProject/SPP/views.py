# views.py

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Announcement
  
from .models import Student     
from .models import Meeting
from .forms import LoginForm
from .models import Proctor

def proctor_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                proctor = Proctor.objects.get(user=user)
                login(request, user)
                request.session['proctor_batch'] = proctor.proctor_batch  # Store proctor's batch in session
                return redirect('proctor_dashboard')  # Redirect to proctor dashboard
            else:
                error_message = "Invalid username or password."
                return render(request, 'login_page.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login_page.html', {'form': form})
# Render the index page with the search form
def logout_view(request):
    logout(request)
    return render(request, 'login_page.html')
@login_required
def proctor_dashboard(request):
    proctor_batch = request.session.get('proctor_batch')
    students = Student.objects.filter(proctor_batch=proctor_batch)
    return render(request, 'proctor_dashboard.html', {'students': students})
@login_required
def index(request):
    # Your view logic goes here
    return render(request, 'index.html')
def announcement(request):
    # Your view logic goes here
    return render(request, 'announcement.html')

def about(request):
    # Your view logic goes here
    return render(request, 'about.html')
@login_required
def login_page(request):
    # Your view logic goes here
    return render(request, 'login_page.html')
@login_required
def meeting(request):
    # Your view logic goes here
    return render(request, 'meeting.html')
@login_required
def schedule_meeting(request):
    if request.method == 'POST':
        meeting_date = request.POST.get('meetingDate')
        meeting_time = request.POST.get('meetingTime')
        reason = request.POST.get('reason')
        
        # Create a Meeting object and save it to the database
        meeting = Meeting(date=meeting_date, time=meeting_time, reason=reason)
        meeting.save()
        
        # Redirect to a success page or homepage
        return redirect('index')  # Adjust the URL name as per your project

    return render(request, 'schedule_meeting.html') 

@login_required
def search_results(request):
    # Retrieve the search query from the GET parameters
    query = request.GET.get('query')
    proctor_batch = request.session.get('proctor_batch')

    # Perform the search by filtering Student objects based on the name field and proctor's batch
    if query:
        # Use case-insensitive search using 'icontains'
        results = Student.objects.filter(name__icontains=query, proctor_batch=proctor_batch)
    else:
        # If no query is provided, return an empty queryset
        results = []

    # Pass the search results to the template for rendering
    return render(request, 'search_results.html', {'query': query, 'results': results})

def get_latest_announcements(request):
    # Retrieve latest announcements
    latest_announcements = Announcement.objects.order_by('-created_at')[:10]

    # Convert announcements to JSON format
    announcements_data = [{
        'title': announcement.title,
        'content': announcement.content,
    } for announcement in latest_announcements]

    # Return JSON response
    return JsonResponse({'announcements': announcements_data})