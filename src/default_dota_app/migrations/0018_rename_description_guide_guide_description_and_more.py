# Generated by Django 5.1.1 on 2024-09-16 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0017_rename_description_item_item_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guide',
            old_name='description',
            new_name='guide_description',
        ),
        migrations.AddField(
            model_name='guide',
            name='hero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='default_dota_app.hero'),
        ),
    ]