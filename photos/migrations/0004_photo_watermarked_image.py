# Generated by Django 4.2.6 on 2023-12-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_rename_discription_photo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='watermarked_image',
            field=models.ImageField(blank=True, null=True, upload_to='watermarked_images'),
        ),
    ]