# Generated by Django 4.1.2 on 2022-10-29 07:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='app.subject'),
            preserve_default=False,
        ),
    ]
