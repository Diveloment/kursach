# Generated by Django 4.1.1 on 2022-11-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_email_verify_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.CharField(default='клиент', max_length=55),
        ),
    ]