# Generated by Django 3.2.3 on 2021-07-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210708_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postresiimage',
            name='images',
            field=models.ImageField(upload_to='resipage_nav/images/'),
        ),
    ]