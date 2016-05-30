# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='BMS.Post', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='BMS.Account', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='BMS.Account', default=1),
            preserve_default=False,
        ),
    ]
