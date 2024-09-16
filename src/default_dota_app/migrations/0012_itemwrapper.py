# Generated by Django 5.1.1 on 2024-09-15 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0011_talentwrapper'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemWrapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explanation', models.TextField(blank=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='default_dota_app.item')),
            ],
        ),
    ]
