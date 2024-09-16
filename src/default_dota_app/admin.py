from django.contrib import admin
from default_dota_app.models import *

# Register your serializers here.

admin.site.register(Hero)
admin.site.register(Item)
admin.site.register(Talent)
admin.site.register(Skill)
admin.site.register(TalentWrapper)
admin.site.register(ItemWrapper)
admin.site.register(Stage)
admin.site.register(SkillBuild)
admin.site.register(Guide)
