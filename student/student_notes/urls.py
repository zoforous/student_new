from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from notes import views as note_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', note_views.register, name='register'),

    # Notes app
    path('', include('notes.urls')),  # Includes note list, detail, create, etc.
]