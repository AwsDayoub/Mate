# Generated by Django 4.1.2 on 2022-10-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='images/default/user.png', null=True, upload_to='images/'),
        ),
    ]
