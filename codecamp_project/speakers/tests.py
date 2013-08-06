from django.test import TestCase


class SpeakersViewsTestCase(TestCase):
    fixtures = ['speakers_views_testdata.json']

    def test_index(self):
        """
        tests the speaker index view
        """
        resp = self.client.get('/speakers/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('speakers' in resp.context)
        self.assertEqual([speaker.pk for speaker in resp.context['speakers']], [1])
        speaker_1 = resp.context['speakers'][0]
        self.assertEqual(speaker_1.first_name, 'Tyler')
        self.assertEqual(speaker_1.last_name, 'Harms')
        self.assertEqual(speaker_1.slug, 'tyler-harms')

    def test_detail_redirect(self):
        """
        tests the speaker detail redirect
        """
        resp = self.client.get('/speakers/1/')
        self.assertEqual(resp.status_code, 302)

        # Ensure that non-existent speaker throw a 404.
        resp = self.client.get('/speakers/2/')
        self.assertEqual(resp.status_code, 404)

    def test_detail(self):
        """
        tests the speaker detail view
        """
        resp = self.client.get('/speakers/tyler-harms,1/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['speaker'].pk, 1)
        self.assertEqual(resp.context['speaker'].first_name, 'Tyler')
        self.assertEqual(resp.context['speaker'].last_name, 'Harms')
        self.assertEqual(resp.context['speaker'].slug, 'tyler-harms')

        # Ensure that non-existent speaker throw a 404.
        resp = self.client.get('/speakers/tyler-harms,2/')
        self.assertEqual(resp.status_code, 404)
