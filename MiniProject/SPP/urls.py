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
    # urls.py


    path('certificate/add/', views.add_certificate, name='add_certificate'),
    path('certificate/status/', views.check_certificate_status, name='check_certificate_status'),
    path('certificate/view/', views.view_certificate, name='view_certificate'),
    path('marksheet/add/', views.add_marksheet, name='add_marksheet'),
    path('marksheet/view/', views.view_marksheet, name='view_marksheet'),
    # Add other URL patterns as needed
]

     
   

