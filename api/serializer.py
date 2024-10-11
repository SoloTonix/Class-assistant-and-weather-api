from rest_framework import serializers
from core.models import Note

class NoteSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'content', 'created', 'author']