# Generated by Django 5.1.1 on 2024-09-16 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0023_alter_itemwrapper_item_wrapper_explanation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemwrapper',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_wrappers', to='default_dota_app.stage'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='guide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='default_dota_app.guide'),
        ),
    ]
