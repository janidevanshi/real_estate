# Generated by Django 3.2.3 on 2021-06-29 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_photos_commercial_floorplan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commercial',
            old_name='comstruction_status',
            new_name='construction_status',
        ),
    ]