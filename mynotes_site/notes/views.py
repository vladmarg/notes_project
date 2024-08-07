from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, reverse, redirect

from .forms import NoteForm, SubtasksForm
from .models import Note, Subtasks


def all_notes(request: HttpRequest) -> HttpResponse:
    context = {
        'notes': Note.objects.all().prefetch_related('subtasks_set'),
    }
    return render(request, 'notes/all_notes.html', context=context)


def create_note(request: HttpRequest) -> HttpResponse:
    if request.POST:
        form = NoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(**form.cleaned_data)
            url = reverse('notes:all_notes')
            return redirect(url)
    context = {
        'form': NoteForm(),
    }
    return render(request, 'notes/create_note.html', context=context)


def delete_notes(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        note_ids = request.POST.getlist('is_delete')
        Note.objects.filter(id__in=note_ids).delete()
        url = reverse('notes:all_notes')
        return redirect(url)
    context = {
        'notes': Note.objects.all(),
    }
    return render(request, 'notes/delete_notes.html', context=context)


def add_subtask(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        note_id = request.POST.get('is_selected')
        url = reverse('notes:add_subtask_for_id', args=(note_id,))
        return redirect(url)
    context = {
        'notes': Note.objects.all(),
    }
    return render(request, 'notes/add_subtask.html', context=context)


def add_subtask_for_id(request: HttpRequest, note_id: int) -> HttpResponse:
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        form = SubtasksForm(request.POST)
        if form.is_valid():
            Subtasks.objects.create(title=form.cleaned_data['title'], note=note)
            url = reverse('notes:all_notes')
            return redirect(url)
    context = {
        'note': note,
        'note_id': note_id,
        'form': SubtasksForm(),
    }
    return render(request, 'notes/add_subtask_for_id.html', context=context)
