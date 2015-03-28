# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('picture', stdimage.fields.StdImageField(upload_to=b'gallery/GalleryImages')),
                ('description', models.TextField(blank=True)),
                ('created', models.TimeField(auto_now_add=True)),
                ('modified', models.TimeField(auto_now=True)),
                ('gallery', models.ForeignKey(to='gallery.Gallery')),
            ],
            options={
                'ordering': ('created',),
                'get_latest_by': ('created',),
                'verbose_name': 'Gallery Picture',
                'verbose_name_plural': 'Gallery Pictures',
            },
            bases=(models.Model,),
        ),
    ]
