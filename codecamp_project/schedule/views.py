from django.template import RequestContext, loader
from django.http import HttpResponse


def index(request):
    speaker_list = object()
    session_list = object()
    t = loader.get_template('schedule/index.html')
    c = RequestContext(request, {
        'speaker_list': speaker_list,
        'session_list': session_list,
        'request': request})
    response = HttpResponse(t.render(c))
    return response
