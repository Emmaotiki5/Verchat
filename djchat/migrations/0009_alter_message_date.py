# Generated by Django 4.1.10 on 2023-07-07 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djchat', '0008_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 7, 20, 55, 20, 895766)),
        ),
    ]
