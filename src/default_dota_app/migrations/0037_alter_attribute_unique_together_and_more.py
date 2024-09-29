import django.core.validators
from django.db import migrations, models

import default_dota_app.models.attribute_model


class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0036_alter_attribute_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='display_order',
            field=models.IntegerField(
                default=default_dota_app.models.attribute_model.get_next_display_order,
                validators=[django.core.validators.MinValueValidator(1)],
            ),
        ),
    ]
