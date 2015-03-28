__author__ = 'ben'
from django.db import models
from stdimage import StdImageField
from mcindoe2_0.models import BasePageObject

class Gallery(BasePageObject):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Picture(models.Model):
    title =             models.CharField(max_length=255, blank=False)
    picture =           StdImageField(upload_to='static/gallery/pictures', blank=False, size=(640, 480), thumbnail_size=(100, 100))
    description =       models.TextField(blank=True)
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    gallery = models.ForeignKey(Gallery)
    ordering = models.SmallIntegerField()
    def __unicode__(self):
        return self.title

    class Meta():
        ordering = ('-ordering','created',)
        get_latest_by = ('created',)
        verbose_name = 'Gallery Picture'
        verbose_name_plural = 'Gallery Pictures'

