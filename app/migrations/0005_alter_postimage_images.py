# Generated by Django 3.2.4 on 2021-07-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210708_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='<django.db.models.query_utils.DeferredAttribute object at 0x000001C8F10EBE80>/post_images/'),
        ),
    ]
