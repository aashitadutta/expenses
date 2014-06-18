# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyexpenses',
            name='Name',
            field=models.CharField(default=b'Null', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weeklyexpenses',
            name='Travel_fare',
            field=models.IntegerField(default=10),
        ),
    ]
