# Generated by Django 5.1.1 on 2024-09-22 11:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0033_alter_attribute_options_attribute_display_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='display_order',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
