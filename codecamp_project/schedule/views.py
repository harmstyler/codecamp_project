from django.shortcuts import render
from django.http import Http404
from django import template

from campsessions.models import Room, Time

register = template.Library()

def index(request):
    try:
        rooms = Room.objects.all()
        times = Time.objects.all().order_by('time')
        # session_list = Session.objects.values().order_by('time', 'room')
    except Time.DoesNotExist:
        raise Http404
    return render(request, 'schedule/index.html',
        {'rooms': rooms, 'times': times})
