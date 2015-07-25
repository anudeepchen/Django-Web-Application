# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_failedlogin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='failedlogin',
            name='username',
        ),
        migrations.AddField(
            model_name='failedlogin',
            name='email',
            field=models.EmailField(max_length=254, default='', unique=True),
        ),
    ]
