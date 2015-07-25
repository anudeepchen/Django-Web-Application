# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_register_acc_locked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='acc_locked',
            field=models.BooleanField(default=False),
        ),
    ]
