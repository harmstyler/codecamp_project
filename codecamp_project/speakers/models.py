from django.db import models


class Speaker(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
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