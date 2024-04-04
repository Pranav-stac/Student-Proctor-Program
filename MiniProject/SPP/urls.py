from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('index/', views.index, name='index'),
    path('search/', views.search_results, name='search_results'),
    path('meeting/', views.meeting, name='meeting'),
    path('schedule_meeting/', views.schedule_meeting, name='schedule_meeting'),
    path('about/', views.about, name='about'),
    path('proctor_login/', views.proctor_login, name='proctor_login'),
    path('proctor_dashboard/', views.proctor_dashboard, name='proctor_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('announcement/', views.announcement, name='announcement'),
    path('get_latest_announcements/', views.get_latest_announcements, name='get_latest_announcements'), 
    path('certificate/', views.certificate, name='certificate'),
    path('certificate/add/', views.add_certificate, name='add_certificate'),
    path('certificate/view/', views.view_certificate, name='view_certificate'),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/', views.get_messages, name='get_messages'),
    path('get_certificates/', views.get_certificates, name='get_certificates'),
    path('certificate/<int:certificate_id>/', views.view_certificate, name='view_certificate'),
    path('get_schedule_meetings/', views.get_schedule_meetings, name='get_schedule_meetings'),
    path('upload_announcement/', views.upload_announcement, name='upload_announcement'),
]

