# Generated by Django 4.0.6 on 2022-07-25 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_contact_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Birthdate',
            field=models.DateField(default=datetime.datetime(2022, 7, 25, 11, 14, 6, 364700)),
        ),
    ]
