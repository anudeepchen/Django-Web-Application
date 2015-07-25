# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_failedlogin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='failedlogin',
            name='user',
        ),
        migrations.AddField(
            model_name='failedlogin',
            name='username',
            field=models.CharField(max_length=120, default=''),
        ),
    ]
