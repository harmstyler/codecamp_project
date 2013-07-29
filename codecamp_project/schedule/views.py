from django.shortcuts import render
from django.http import Http404

from campsessions.models import Session


def index(request):
    try:
        sessions = Session.objects.all().order_by('time')
    except Session.DoesNotExist:
        raise Http404
    return render(request, 'schedule/index.html', {'sessions': sessions})
