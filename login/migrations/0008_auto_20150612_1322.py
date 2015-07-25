# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150612_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failedlogin',
            name='email',
            field=models.EmailField(max_length=254, default=''),
        ),
    ]
