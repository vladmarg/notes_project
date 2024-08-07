from django import forms


class NoteForm(forms.Form):
    title = forms.CharField()


class SubtasksForm(forms.Form):
    title = forms.CharField()
