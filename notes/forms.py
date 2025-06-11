from django import forms
from .models import Note, Subject


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'subject', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }


# Optional: for adding subjects via a form interface
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }