from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .models import Note
from .forms import NoteForm

def index(request):
    return render(request, 'myapp/navigation.html')

def note(request):
    return HttpResponse(f'{note.title} {note.text}; ' for note in Note.objects.all())

def test(request):
    return HttpResponse('test page')

@api_view(['POST'])
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'myapp/add_note.html', {'form': form})
    #Note.objects.create(title=title, text=text)