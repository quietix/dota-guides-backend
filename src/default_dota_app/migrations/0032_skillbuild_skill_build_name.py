# Generated by Django 5.1.1 on 2024-09-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0031_remove_skillbuild_skill_build_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillbuild',
            name='skill_build_name',
            field=models.CharField(default='', max_length=300),
        ),
    ]
