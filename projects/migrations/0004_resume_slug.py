# Generated by Django 5.2 on 2025-04-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
