# Generated by Django 5.1.1 on 2024-09-22 10:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0029_skillbuild_skillorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillorder',
            name='learning_order',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
