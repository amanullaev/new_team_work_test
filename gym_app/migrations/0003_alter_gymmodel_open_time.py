# Generated by Django 4.2.5 on 2023-09-11 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0002_gymmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymmodel',
            name='open_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 11, 16, 49, 16, 759309)),
        ),
    ]
