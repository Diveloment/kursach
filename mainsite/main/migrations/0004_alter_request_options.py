# Generated by Django 4.1.1 on 2022-12-04 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_request_leads_alter_request_createdby'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'field', 'verbose_name_plural': 'fields'},
        ),
    ]
