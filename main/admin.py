from django.contrib import admin

# Register your models here.

from .models import Cars


class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'color',
                    'city', 'country', 'price', 'currency')


admin.site.register(Cars, CarsAdmin)