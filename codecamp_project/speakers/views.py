from django.shortcuts import render
from django.http import Http404
from django import template

from speakers.models import Speaker

register = template.Library()

def index(request):
    try:
        speakers = Speaker.objects.all()
    except Speaker.DoesNotExist:
        raise Http404
    return render(request, 'speakers/index.html',
        {'speakers': speakers})
