# Generated by Django 3.1.7 on 2021-03-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='uname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
