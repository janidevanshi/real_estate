# Generated by Django 3.2.3 on 2021-07-09 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_postresiimage_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residential',
            name='slug',
        ),
        migrations.AlterField(
            model_name='residential',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
