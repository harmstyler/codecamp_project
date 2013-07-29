from django.db import models
from django.template.defaultfilters import slugify

from core.models import TimeStampedModel
from speakers.models import Speaker


class Room(TimeStampedModel):
    """
    Room model docstring
    """
    name = models.CharField(max_length=60)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Session(TimeStampedModel):
    """
    Session model docstring
    """
    speakers = models.ManyToManyField(Speaker)
    title = models.CharField(max_length=60)
    abstract = models.TextField(blank=True,)
    time = models.TimeField()
    room = models.ForeignKey(Room, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        return super(Session, self).save(*args, **kwargs)
