# Generated by Django 4.2.5 on 2023-09-10 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yangilik', '0004_alter_new_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 10, 22, 17, 33, 696735)),
        ),
    ]
