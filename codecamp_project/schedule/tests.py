from django.test import TestCase


class ScheduleViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/schedule/')
        self.assertEqual(resp.status_code, 200)
