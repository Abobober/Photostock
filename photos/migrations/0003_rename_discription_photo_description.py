# Generated by Django 4.2.6 on 2023-12-10 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_discription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='discription',
            new_name='description',
        ),
    ]
