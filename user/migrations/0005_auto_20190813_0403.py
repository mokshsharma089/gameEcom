# Generated by Django 2.2.3 on 2019-08-13 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190813_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='games_rented',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Games'),
        ),
    ]