from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note, Subject
from .forms import NoteForm

# ----- USER REGISTRATION -----
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'notes/register.html', {'form': form})


# ----- CRUD VIEWS FOR NOTES -----
class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).order_by('-created_at')


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


# ----- SHARE NOTE (VIEW ONLY) -----
@login_required
def share_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    # In production, implement permission logic here
    return render(request, 'notes/note_detail.html', {'note': note})


# ----- OPTIONAL: Filter notes by subject -----
@login_required
def notes_by_subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    notes = Note.objects.filter(owner=request.user, subject=subject)
    return render(request, 'notes/note_list.html', {'notes': notes})
