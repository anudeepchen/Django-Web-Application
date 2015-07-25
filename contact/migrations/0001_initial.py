# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=120)),
                ('last_name', models.CharField(default='', max_length=120)),
                ('email', models.EmailField(help_text="The format of your email should be 'youremail@something.com'", default='', max_length=254)),
                ('phone', models.CharField(validators=[django.core.validators.RegexValidator(regex='^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}$')], help_text="Phone number must be entered in the format: '+9 9999999999'. Up to 15 digits allowed.", max_length=15, default='')),
                ('interest', models.CharField(default='CL', max_length=2, choices=[('CL', 'Client'), ('IN', 'Investor'), ('PA', 'Partner'), ('AC', 'Academic'), ('OT', 'Other')])),
                ('message', models.TextField(default='', max_length=250)),
            ],
        ),
    ]
