# Generated by Django 4.1.1 on 2022-12-19 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_feedback_feedbackcreatedby'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'отзыв', 'verbose_name_plural': 'отзывы'},
        ),
    ]
