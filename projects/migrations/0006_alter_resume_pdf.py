# Generated by Django 5.2 on 2025-04-06 00:23

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_resume_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='pdf',
            field=models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='resumes/'),
        ),
    ]
