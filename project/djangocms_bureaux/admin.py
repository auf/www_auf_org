from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import BureauExtension, Region


class BureauExtensionAdmin(PageExtensionAdmin):
    pass

class RegionAdmin(admin.ModelAdmin):
    pass
admin.site.register(BureauExtension, BureauExtensionAdmin)
admin.site.register(Region, RegionAdmin)
