# Generated by Django 5.1.1 on 2024-09-16 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0020_remove_talentwrapper_guide_remove_skillbuild_guide_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_title', models.CharField(max_length=200)),
                ('guide_description', models.TextField()),
                ('hero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='default_dota_app.hero')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=200)),
                ('stage_description', models.TextField(blank=True)),
                ('guide', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='default_dota_app.guide')),
            ],
        ),
        migrations.CreateModel(
            name='ItemWrapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_wrapper_explanation', models.CharField(max_length=200)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='default_dota_app.item')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='default_dota_app.stage')),
            ],
        ),
    ]