# Generated by Django 4.1.1 on 2022-12-04 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[('admin', 'админ'), ('client', 'клиент'), ('eng', 'инжинер')], default='client', max_length=55),
        ),
    ]
