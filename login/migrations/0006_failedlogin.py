# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_delete_failedlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='FailedLogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=120, default='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
