# Generated by Django 2.2.14 on 2021-12-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20211216_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='time',
            field=models.TimeField(blank=True, default='', null=True),
        ),
    ]
