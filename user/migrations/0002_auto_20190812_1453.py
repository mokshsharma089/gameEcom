# Generated by Django 2.2.3 on 2019-08-12 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='games_rented',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Games'),
        ),
    ]
