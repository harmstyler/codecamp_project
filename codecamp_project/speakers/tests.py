from django.test import TestCase


class SpeakersViewsTestCase(TestCase):
    fixtures = ['speakers_views_testdata.json']

    def test_index(self):
        resp = self.client.get('/speakers/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('speakers' in resp.context)
        self.assertEqual([speaker.pk for speaker in resp.context['speakers']], [1])
        speaker_1 = resp.context['speakers'][0]
        self.assertEqual(speaker_1.first_name, 'Tyler')
        self.assertEqual(speaker_1.last_name, 'Harms')
        self.assertEqual(speaker_1.slug, 'tyler-harms')
