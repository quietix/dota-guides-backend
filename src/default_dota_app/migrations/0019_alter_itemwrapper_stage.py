# Generated by Django 5.1.1 on 2024-09-16 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0018_rename_description_guide_guide_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemwrapper',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemwrappers', to='default_dota_app.stage'),
        ),
    ]
