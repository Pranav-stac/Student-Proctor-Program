from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, CertificateForm
from .models import Announcement, Student, Meeting, Proctor, Message, Certificate

def get_schedule_meetings(request):
    meetings = Meeting.objects.all()
    meetings_data = [{'date': meeting.date, 'time': meeting.time, 'reason': meeting.reason} for meeting in meetings]
    return JsonResponse({'meetings': meetings_data})

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

# Logout view
def logout_view(request):
    logout(request)
    return render(request, 'login_page.html')

# Proctor dashboard view
@login_required
def proctor_dashboard(request):
    proctor_batch = request.session.get('proctor_batch')
    students = Student.objects.filter(proctor_batch=proctor_batch)
    return render(request, 'proctor_dashboard.html', {'students': students})

# Index view
@login_required
def index(request):
    # Your view logic goes here
    return render(request, 'index.html')

# Announcement view
@login_required
def announcement(request):
    # Your view logic goes here
    return render(request, 'announcement.html')

# About view
@login_required
def about(request):
    # Your view logic goes here
    return render(request, 'about.html')

# Login page view

def login_page(request):
    # Your view logic goes here
    return render(request, 'login_page.html')

# Meeting view
@login_required
def meeting(request):
    # Your view logic goes here
    return render(request, 'meeting.html')

# Schedule meeting view
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

# Search results view
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

# Get latest announcements API view
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

# Certificate view
def certificate(request):
    return render(request, 'certificate.html')

# Send message API view
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        message = request.POST.get('message')
        Message.objects.create(sender=sender, message=message)
        return JsonResponse({'status': 'OK'})

# Get messages API view
def get_messages(request):
    messages = Message.objects.all().values()
    return JsonResponse(list(messages), safe=False)

# Add certificate view
def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to the certificate page
            return redirect('certificate')  # Assuming 'certificate' is the URL name for the certificate page
    else:
        form = CertificateForm()
    return render(request, 'add_certificate.html', {'form': form})

# View certificate view
def view_certificate(request, certificate_id):
    try:
        certificate = Certificate.objects.get(id=certificate_id)
        return render(request, 'view_certificate.html', {'certificate': certificate})
    except Certificate.DoesNotExist:
        return HttpResponse("Certificate not found")

# Get certificates API view
def get_certificates(request):
    # Retrieve all certificates from the database
    certificates = Certificate.objects.all()

    # Serialize certificates data
    certificates_data = [{'certificate_name': cert.certificate_name, 'image_url': cert.image.url} for cert in certificates]

    # Return the serialized data as JSON response
    return JsonResponse(certificates_data, safe=False)