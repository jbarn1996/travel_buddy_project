# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20171026_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='friends',
            field=models.ManyToManyField(related_name='_owner_friends_+', to='login_app.Owner'),
        ),
    ]
