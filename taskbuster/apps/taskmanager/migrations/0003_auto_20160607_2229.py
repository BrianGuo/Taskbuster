# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20160607_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('user', models.ForeignKey(related_name='tags', verbose_name='user', to='taskmanager.Profile')),
            ],
            options={
                'ordering': ('user', 'name'),
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('user', 'name')]),
        ),
    ]
