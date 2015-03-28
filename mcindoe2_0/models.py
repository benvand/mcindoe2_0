from django.db import models


class BasePageObject(models.Model):
    page_name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.page_name

    class Meta:
        abstract = True
