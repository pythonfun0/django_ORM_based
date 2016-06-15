# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starter_app', '0002_auto_20160609_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-date_of_creation']},
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='date_of_createion',
            new_name='date_of_creation',
        ),
    ]
