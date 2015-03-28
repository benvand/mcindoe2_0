# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150328_1011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ('-ordering', 'created'), 'get_latest_by': ('created',), 'verbose_name': 'Gallery Picture', 'verbose_name_plural': 'Gallery Pictures'},
        ),
        migrations.AddField(
            model_name='picture',
            name='ordering',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='content',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=stdimage.fields.StdImageField(upload_to=b'static/gallery/pictures'),
            preserve_default=True,
        ),
    ]
