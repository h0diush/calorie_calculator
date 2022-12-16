from django.contrib import admin

from .models import CaloriesModel


@admin.register(CaloriesModel)
class CaloriesModelAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'food', 'qty_calories', 'created'
    )
    list_filter = ('user',)
    search_fields = ('food', 'user')
