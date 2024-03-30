# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('search/', views.search_results, name='search_results'),
    path('meeting/', views.meeting, name='meeting'),
    path('schedule_meeting/', views.schedule_meeting, name='schedule_meeting'),
    path('about', views.about, name='about'),
    path('login/',views.login_page,name='login_page'),
    path('', views.proctor_login, name='proctor_login'),
    path('proctor_dashboard/', views.proctor_dashboard, name='proctor_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('announcement/', views.announcement, name='announcement'),
    path('get_latest_announcements/', views.get_latest_announcements, name='get_latest_announcements'), 
<<<<<<< HEAD
    # urls.py


    path('certificate/add/', views.add_certificate, name='add_certificate'),
    path('certificate/status/', views.check_certificate_status, name='check_certificate_status'),
    path('certificate/view/', views.view_certificate, name='view_certificate'),
    path('marksheet/add/', views.add_marksheet, name='add_marksheet'),
    path('marksheet/view/', views.view_marksheet, name='view_marksheet'),
    # Add other URL patterns as needed
]
=======
    path('', views.index, name='index'),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/', views.get_messages, name='get_messages'),
>>>>>>> 4aecfee61da946b0acc68c3ee74af3d3af2a45ca

     
   

