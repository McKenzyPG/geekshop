# Generated by Django 2.0.1 on 2018-01-08 04:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0020_auto_20180106_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 10, 4, 40, 55, 706064, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
