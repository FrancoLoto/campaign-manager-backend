from django.contrib import admin

from .models import Campaign, Subscriber


class CampaignAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_per_page = 25


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "campaign", "created_at", "updated_at")
    search_fields = ("email", "campaign__title")
    list_per_page = 25


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
