from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Note
from .forms import NoteForm

# sirf logged-in users apne notes dekh sakte hain
@login_required
def note_list(request):
    # sirf current user ke notes fetch kar rahe hain
    notes = Note.objects.filter(owner=request.user)
    return render(request, 'note_list.html', {'notes': notes})


# naya note create karna
@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            # note ka owner current user set kar rahe hain
            note.owner = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'note_form.html', {'form': form})


# note edit karna (sirf apna note edit kar sakta hai)
@login_required
def note_edit(request, pk):
    # ensure kar rahe hain ke user sirf apna note hi access kare
    note = get_object_or_404(Note, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'note_form.html', {'form': form})


# note delete karna (sirf apna note delete kar sakta hai)
@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)

    if request.method == 'POST':
        note.delete()
        return redirect('note_list')

    return render(request, 'note_confirm_delete.html', {'note': note})


# user registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})