# Generated by Django 3.2.4 on 2021-07-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210708_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercial',
            name='floorplan',
            field=models.ImageField(default='none', upload_to='folder_str/floorplan_image/'),
        ),
        migrations.AlterField(
            model_name='commercial',
            name='main_image',
            field=models.ImageField(default='none', upload_to='folder_str/main_image'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='folder_str/post_images/'),
        ),
    ]
