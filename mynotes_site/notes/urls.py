from django.urls import path

from .views import all_notes, create_note, delete_notes, add_subtask, add_subtask_for_id

app_name = 'notes'

urlpatterns = [
    path('', all_notes, name='all_notes'),
    path('create/', create_note, name='create_note'),
    path('delete/', delete_notes, name='delete_selected'),
    path('addsub/', add_subtask, name='add_subtask'),
    path('add_subtask_for_id/<int:note_id>/', add_subtask_for_id, name='add_subtask_for_id'),
]
