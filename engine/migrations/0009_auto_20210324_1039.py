# Generated by Django 3.1.7 on 2021-03-24 03:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0008_auto_20210324_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaker',
            name='time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
