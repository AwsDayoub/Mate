# Generated by Django 4.1.2 on 2022-10-29 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_message_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
    ]
