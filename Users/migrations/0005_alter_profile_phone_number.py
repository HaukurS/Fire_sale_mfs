# Generated by Django 4.0.4 on 2022-05-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_remove_profile_password_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
