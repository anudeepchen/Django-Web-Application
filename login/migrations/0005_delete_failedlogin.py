# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20150611_1731'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FailedLogin',
        ),
    ]
