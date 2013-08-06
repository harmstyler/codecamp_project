from django.test import TestCase

from templatetags import core_extras
from campsessions.models import Room, Time


class CoreFuntionsTestCase(TestCase):
    fixtures = ['sessions_testdata.json']

    def testShowSession(self):
        room = Room()
        room.id = 1
        time = Time()
        time.id = 1
        core_extras.show_session(room, time)
