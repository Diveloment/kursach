# Generated by Django 4.1.1 on 2022-12-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_request_leads'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
