# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_userinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='acc_locked',
            field=models.BooleanField(default=True),
        ),
    ]
