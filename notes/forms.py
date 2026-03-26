from django import forms
from .models import Note

# Note ke liye ModelForm bana rahe hain
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'color']