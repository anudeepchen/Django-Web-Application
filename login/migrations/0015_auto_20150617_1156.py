# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20150617_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(null=True, max_length=128, default=''),
        ),
    ]
