from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

def index(request):
    return HttpResponse(f'{note.title} {note.text} ' for note in Note.objects.all())