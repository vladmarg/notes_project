from django.db import models


class Subtasks(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey('Note', on_delete=models.CASCADE)


class Note(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
