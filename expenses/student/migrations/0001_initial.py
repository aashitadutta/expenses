# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyExpenses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Travel_fare', models.IntegerField(max_length=10)),
                ('Eatables', models.IntegerField(max_length=10)),
                ('Sports', models.IntegerField(max_length=10)),
                ('Accessories', models.IntegerField(max_length=10)),
                ('Total', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
