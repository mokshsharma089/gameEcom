# Generated by Django 2.2.3 on 2019-07-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_games_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='brand_new',
        ),
        migrations.AddField(
            model_name='games',
            name='trailer_id',
            field=models.CharField(default='GoyGlyrYb9c', max_length=20),
        ),
    ]
