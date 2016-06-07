# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('interaction', models.PositiveIntegerField(verbose_name='interaction', default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='profile')),
            ],
            options={
                'verbose_name_plural': 'Profiles',
                'ordering': ('user',),
                'verbose_name': 'Profile',
            },
        ),
    ]
