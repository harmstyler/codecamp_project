from django.shortcuts import render
from django.http import Http404
from django import template

from campsessions.models import Session, Room

register = template.Library()

def index(request):
    try:
        rooms = Room.objects.all()
        sessions = Session.objects.all().order_by('time')
        sessions.query.group_by = ['time']
        # session_list = Session.objects.values().order_by('time', 'room')
    except Session.DoesNotExist:
        raise Http404
    return render(request, 'schedule/index.html',
        {'rooms': rooms, 'sessions': sessions})
