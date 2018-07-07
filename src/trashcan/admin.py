from django.contrib import admin

from .models import TrashCan, Level, Harvest


@admin.register(TrashCan)
class TrashCanAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'barcode',
        'depth',
        'address',
        'lat',
        'lng',
    )
    list_filter = (
        'depth',
    )
    search_fields = (
        'barcode',
        'address',
    )


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'trash_can',
        'time',
        'distance',
    )
    list_filter = (
        'trash_can',
    )


@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'trash_can',
        'date',
        'status',
    )
    list_filter = (
        'status',
    )
