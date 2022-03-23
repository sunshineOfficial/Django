from django.contrib import admin
from rating.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "user", "item")
    list_display_links = ("star", "user", "item")
