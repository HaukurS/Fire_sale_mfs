# Generated by Django 4.0.4 on 2022-05-09 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_rename_user_profile'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemoffer',
            old_name='price',
            new_name='item_price',
        ),
        migrations.AddField(
            model_name='itemoffer',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemoffer',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.profile'),
        ),
        migrations.AlterField(
            model_name='itemoffer',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.profile'),
        ),
    ]
