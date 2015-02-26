from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import BureauExtension, Region, ImageExtension


class BureauExtensionAdmin(PageExtensionAdmin):
    pass

class RegionAdmin(admin.ModelAdmin):
    pass

class ImageExtensionAdmin(PageExtensionAdmin):
    pass
    
admin.site.register(BureauExtension, BureauExtensionAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(ImageExtension, ImageExtensionAdmin)
  

