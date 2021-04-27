from django.contrib import admin
from .models import Services, Review


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'image',
    )

    ordering = ('sku',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'service',
        'date_reviewed',
        'user',
        'title',
        'stars',
    )


admin.site.register(Services, ServicesAdmin)
admin.site.register(Review, ReviewAdmin)
