# Generated by Django 4.1.10 on 2023-07-06 21:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djchat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 6, 22, 45, 24, 288560)),
        ),
    ]
