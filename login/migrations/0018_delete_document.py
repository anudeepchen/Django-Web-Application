# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_delete_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]
