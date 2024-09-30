from django.core.validators import MinValueValidator
from django.db import migrations, models
from django.db.models import Max


def get_next_display_order():
    from default_dota_app.models import Attribute
    max_order = Attribute.objects.aggregate(Max('display_order'))['display_order__max']
    return (max_order + 1) if max_order is not None else 1

class Migration(migrations.Migration):

    dependencies = [
        ('default_dota_app', '0035_alter_attribute_display_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='display_order',
            field=models.IntegerField(
                default=get_next_display_order,
                validators=[MinValueValidator(1)]
            ),
        ),
    ]
