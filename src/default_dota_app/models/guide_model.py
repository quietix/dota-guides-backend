from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Max

from default_dota_app.models.hero_model import Hero


def get_admin_user():
    return User.objects.filter(is_superuser=True).first().id or User.objects.filter(is_staff=True).first().id


def get_next_guide_order():
    max_order = Guide.objects.aggregate(Max('display_order'))['display_order__max']
    return (max_order + 1) if max_order is not None else 1


class Guide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_admin_user, related_name='guides')
    hero = models.ForeignKey(Hero, null=True, on_delete=models.SET_NULL, related_name='guides')
    guide_title = models.CharField(max_length=200)
    guide_description = models.TextField(blank=True)
    display_order = models.IntegerField(
        default=get_next_guide_order,
        validators=[
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return f"<{self.user.username}> <{self.hero.hero_name}> <{self.guide_title}> <guide #{self.id}>"

    class Meta:
        ordering = ["hero__hero_name", "display_order"]