from django.contrib import admin
from . import models
from posts import models as pmod
from accounts import models as amod
# Register your models here.
admin.site.register(models.Group)  #is a parent model
admin.site.register(pmod.Post)

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember  #group member is not inline with parent
