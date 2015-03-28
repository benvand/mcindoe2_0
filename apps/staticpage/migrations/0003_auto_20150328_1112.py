# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staticpage', '0002_auto_20150328_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='content',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
