# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starter_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('content', models.TextField()),
                ('date_of_createion', models.DateTimeField()),
            ],
            options={
                'ordering': ['-date_of_createion'],
            },
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
