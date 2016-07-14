from django.contrib import admin
from .models import Carousel, CarouselItem
from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableTabularInline

class CarouselItemTabularInline(SortableTabularInline):
	model = CarouselItem

class CarouselAdmin(SortableAdmin):
	inlines = [CarouselItemTabularInline]
	model = Carousel

admin.site.register(Carousel, CarouselAdmin)
