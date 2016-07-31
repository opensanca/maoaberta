# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 22:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='responsible',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('running', 'running'), ('closed', 'closed')], default='open', max_length=7),
        ),
    ]