# Generated by Django 3.1.7 on 2021-03-24 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0006_breaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaker',
            name='time',
            field=models.DateTimeField(blank=True),
        ),
    ]
