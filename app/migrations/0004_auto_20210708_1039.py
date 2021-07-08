# Generated by Django 3.2.4 on 2021-07-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210708_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercial',
            name='floorplan',
            field=models.ImageField(default='none', upload_to='<django.db.models.fields.AutoField>/floorplan_image/'),
        ),
        migrations.AlterField(
            model_name='commercial',
            name='main_image',
            field=models.ImageField(default='none', upload_to='<django.db.models.fields.AutoField>/main_image/'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='<django.db.models.query_utils.DeferredAttribute object at 0x000001D7106DBE20>/post_images/'),
        ),
    ]