# Generated by Django 4.0 on 2024-01-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20211129_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='../default_profile_a8wxng', upload_to='images/'),
        ),
    ]