# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20150612_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='failedlogin',
            name='ipaddr',
            field=models.CharField(max_length=30, default=''),
        ),
    ]
