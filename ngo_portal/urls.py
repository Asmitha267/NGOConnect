from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # homepage
    path('login/', auth_views.LoginView.as_view(template_name="ngo_portal/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Event CRUD URLs
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='create_event'),
    path('events/<int:id>/edit/', views.event_edit, name='event_edit'),
    path('events/<int:id>/delete/', views.event_delete, name='event_delete'),
    
    # Volunteer application
    path('events/<int:id>/apply/', views.apply_event, name='apply_event'),
    
    # Viewing applications (optional, create this view)
    path('events/<int:id>/applications/', views.view_applications, name='view_applications'),
]
