# Generated by Django 2.2.14 on 2021-12-15 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_city_locality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locality',
            name='country',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Locality',
        ),
    ]
