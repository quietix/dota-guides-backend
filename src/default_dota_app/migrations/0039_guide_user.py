# Generated by Django 5.1.1 on 2024-09-25 11:58

import default_dota_app.models.guide_model
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0038_alter_attribute_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='user',
            field=models.ForeignKey(default=default_dota_app.models.guide_model.get_admin_user, on_delete=django.db.models.deletion.CASCADE, related_name='guides', to=settings.AUTH_USER_MODEL),
        ),
    ]
