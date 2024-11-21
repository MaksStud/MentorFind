from django.contrib import admin
from .models import Advertisement, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
