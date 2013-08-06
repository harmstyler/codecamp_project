from django.shortcuts import render, get_object_or_404, redirect
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

def detailID(request, id):
    speaker = get_object_or_404(Speaker, pk=id)
    return redirect(speaker)

def detail(request, slug, id):
    speaker = get_object_or_404(Speaker, pk=id)
    return render(request, 'speakers/detail.html',
        {'speaker': speaker})