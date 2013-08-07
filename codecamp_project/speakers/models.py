from django.db import models

from core.models import TimeStampedModel

class Speaker(TimeStampedModel):
    """
    Codecamp Speaker Model

    Should contain speaker name, bio, etc based on the needs of the app.
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    twitter_handle = models.CharField(max_length=200,null=True)
    image_url = models.URLField(null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['last_name']

    def _get_full_name(self):
        """Returns the speaker's full name."""
        return '%s %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)

    def __unicode__(self):
        return self.full_name

    def get_absolute_url(self):
        return ('speaker_detail', (), {'slug': self.slug,
                                       'id': self.id})
    get_absolute_url = models.permalink(get_absolute_url)