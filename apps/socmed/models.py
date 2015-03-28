from django.db import models

class SocialMediaBase(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.FileField(upload_to='static/')
    ordering = models.SmallIntegerField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

class SocialMedia(SocialMediaBase):
    pass