# Generated by Django 2.2.14 on 2021-12-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_auto_20211216_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('phone2', models.IntegerField(blank=True)),
                ('email', models.EmailField(max_length=250)),
                ('service_name', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
            ],
        ),
    ]