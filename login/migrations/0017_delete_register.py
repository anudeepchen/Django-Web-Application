# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_auto_20150720_1350'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
    ]
