# Generated by Django 4.1.1 on 2022-12-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_request_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='file',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
    ]
