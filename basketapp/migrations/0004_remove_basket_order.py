# Generated by Django 2.0.1 on 2018-01-10 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0003_auto_20180108_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='order',
        ),
    ]
