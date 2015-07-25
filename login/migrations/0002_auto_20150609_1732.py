# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(default='', max_length=120)),
                ('last_name', models.CharField(default='', max_length=120)),
                ('email', models.EmailField(default='', unique=True, max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128)),
                ('username', models.CharField(default='', max_length=120)),
                ('password', models.CharField(default='', max_length=120)),
                ('reenter_password', models.CharField(default='', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='LoginPage',
        ),
    ]
