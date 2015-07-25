# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_auto_20150617_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128),
        ),
    ]
