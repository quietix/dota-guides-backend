# Generated by Django 5.1.1 on 2024-11-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0049_alter_attribute_attribute_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='display_order',
            field=models.IntegerField(default=100),
        ),
    ]
