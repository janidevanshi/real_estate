# Generated by Django 3.2.3 on 2021-07-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_commercial_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercial',
            name='amenities',
            field=models.TextField(),
        ),
    ]
