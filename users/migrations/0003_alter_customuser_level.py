# Generated by Django 4.1.2 on 2022-10-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='level',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
    ]
