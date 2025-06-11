from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # --- Authentication ---
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # --- Notes CRUD ---
    path('', views.NoteListView.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('notes/new/', views.NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note-delete'),

    # --- Extras ---
    # path('notes/<int:pk>/download/', views.download_note_pdf, name='note-download'),
    path('notes/<int:pk>/share/', views.share_note, name='note-share'),
    path('subject/<int:subject_id>/notes/', views.notes_by_subject, name='notes-by-subject'),
]