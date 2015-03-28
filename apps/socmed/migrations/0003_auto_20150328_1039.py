# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socmed', '0002_socialmedia_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='url',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
