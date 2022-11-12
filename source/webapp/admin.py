from django.contrib import admin
from webapp.models import GuestBook


class AdminGuestBook(admin.ModelAdmin):
    list_display = ["id", "author", "status"]
    list_display_links = ["author"]
    list_filter = ["status"]
    search_fields = ["author", "text"]
    fields = ["author", "email", "status", "text", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]


admin.site.register(GuestBook, AdminGuestBook)
