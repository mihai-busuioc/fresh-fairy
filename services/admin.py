from django.contrib import admin
from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Services, ServicesAdmin)
