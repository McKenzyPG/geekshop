# Generated by Django 2.0.1 on 2018-01-10 05:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0022_auto_20180108_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 12, 5, 18, 9, 687883, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]