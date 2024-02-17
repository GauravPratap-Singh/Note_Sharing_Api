from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    shared_notes = models.ManyToManyField(User, related_name='shared_notes')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class NoteVersion(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='versions')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    changes = models.TextField()
    def __str__(self):
        return self.changes

