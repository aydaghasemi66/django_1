# Generated by Django 4.2.4 on 2023-08-11 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='defualt.jpg', upload_to='course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='schedule',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 16, 21, 53, 383063)),
        ),
    ]
