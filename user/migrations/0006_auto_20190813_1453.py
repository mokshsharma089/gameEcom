# Generated by Django 2.2.3 on 2019-08-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_offers'),
        ('user', '0005_auto_20190813_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='games_rented',
        ),
        migrations.AddField(
            model_name='profile',
            name='games_rented',
            field=models.ManyToManyField(to='home.Games'),
        ),
    ]
