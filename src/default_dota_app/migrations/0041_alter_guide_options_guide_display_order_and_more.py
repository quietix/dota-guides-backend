# Generated by Django 5.1.1 on 2024-09-25 16:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0040_alter_hero_hero_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guide',
            options={'ordering': ['hero__hero_name', 'display_order']},
        ),
        migrations.AddField(
            model_name='guide',
            name='display_order',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='guide',
            name='hero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guides', to='default_dota_app.hero'),
        ),
    ]