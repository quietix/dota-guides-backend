# Generated by Django 5.1.1 on 2024-09-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0042_alter_skillbuild_options_alter_guide_display_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
