# Generated by Django 3.2.3 on 2021-07-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210709_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postresiimage',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]