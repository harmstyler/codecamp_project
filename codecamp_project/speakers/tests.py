from django.test import TestCase


class SpeakersViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/speakers/')
        self.assertEqual(resp.status_code, 200)
