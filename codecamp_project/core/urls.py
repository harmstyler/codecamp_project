# core/urls.py
from django.conf.urls.defaults import patterns
from views import HomeView

urlpatterns = patterns('',
    (r'^', HomeView.as_view()),
)