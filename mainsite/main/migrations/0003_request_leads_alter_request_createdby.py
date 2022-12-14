# Generated by Django 4.1.1 on 2022-12-04 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='leads',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdBy', to=settings.AUTH_USER_MODEL),
        ),
    ]
