# Generated by Django 2.2.14 on 2021-12-16 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20211216_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workers',
            old_name='service_name',
            new_name='service_names',
        ),
    ]
