# Generated by Django 4.0.4 on 2022-05-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
