from django.contrib import admin
from .models_filer import Carousel, CarouselItem
from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableTabularInline

class CarouselItemTabularInline(SortableTabularInline):
	model = CarouselItem
   	fields = ('capion_title', 'caption_content', 'image', 'url', 'the_order')

class CarouselAdmin(SortableAdmin):
	inlines = [CarouselItemTabularInline]
	model = Carousel

admin.site.register(Carousel, CarouselAdmin)
