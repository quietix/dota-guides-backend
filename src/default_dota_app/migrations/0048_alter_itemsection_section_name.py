# Generated by Django 5.1.1 on 2024-10-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0047_item_item_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsection',
            name='section_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
