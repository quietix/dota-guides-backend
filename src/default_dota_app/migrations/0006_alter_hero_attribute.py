# Generated by Django 5.1.1 on 2024-09-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0005_alter_hero_options_hero_attribute_alter_hero_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='attribute',
            field=models.CharField(choices=[('STRENGTH', 'Strength'), ('AGILITY', 'Agility'), ('INTELLIGENCE', 'Intelligence'), ('UNIVERSAL', 'Universal')], default='UNIVERSAL', max_length=20),
        ),
    ]
