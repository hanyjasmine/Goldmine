# Generated by Django 3.1.7 on 2021-03-22 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_auto_20210317_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=100)),
                ('nameloc', models.CharField(blank=True, max_length=100)),
                ('sector', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('likelihood', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'results',
            },
        ),
    ]
