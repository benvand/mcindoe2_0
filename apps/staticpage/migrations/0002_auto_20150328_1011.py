# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staticpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staticpage',
            old_name='name',
            new_name='page_name',
        ),
    ]
