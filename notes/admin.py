from django.contrib import admin
from .models import Note, Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject', 'owner', 'created_at', 'updated_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('title', 'content', 'owner__username')
    ordering = ('-created_at',)