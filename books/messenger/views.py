# messenger/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'messenger/index.html')

def room(request, room_name):
    return render(request, 'messenger/room.html', {
        'room_name': room_name
    })