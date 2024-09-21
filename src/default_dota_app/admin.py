from django.contrib import admin
from default_dota_app.models import *

# Register your serializers here.

admin.site.register(Hero)
admin.site.register(Item)
admin.site.register(Guide)
admin.site.register(ItemWrapper)
admin.site.register(Stage)
admin.site.register(Attribute)