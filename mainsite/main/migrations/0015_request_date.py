# Generated by Django 4.1.1 on 2022-12-18 14:57

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_request_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='date',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now),
        ),
    ]
