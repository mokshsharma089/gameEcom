# Generated by Django 2.2.3 on 2019-12-09 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190813_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='games_rented',
        ),
    ]
