# Generated by Django 4.1.2 on 2022-10-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='prof',
            field=models.CharField(max_length=100),
        ),
    ]