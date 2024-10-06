# Generated by Django 5.1.1 on 2024-10-01 14:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0044_alter_guide_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=200)),
                ('display_order', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]