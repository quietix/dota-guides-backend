# Generated by Django 5.1.1 on 2024-09-22 11:52

import default_dota_app.models.attribute_model
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0034_alter_attribute_display_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='display_order',
            field=models.IntegerField(default=default_dota_app.models.attribute_model.get_next_display_order, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]