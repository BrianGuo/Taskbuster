# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='name', help_text='Enter the project name', max_length=100)),
                ('color', models.CharField(verbose_name='color', default='#fff', validators=[django.core.validators.RegexValidator('(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)')], help_text='Enter the hex color code, like #ccc or #cccccc', max_length=7)),
                ('user', models.ForeignKey(verbose_name='user', to='taskmanager.Profile', related_name='projects')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ('user', 'name'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'name')]),
        ),
    ]
