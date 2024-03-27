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

     
   

]  
