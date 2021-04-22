from django.contrib import admin
from authentication.models import CoreUser
# Register your models here.
@admin.register(CoreUser)
class CoreUserAdmin(admin.ModelAdmin):
    list_display = [ "id", "first_name", "last_name", "is_superuser"]
    search_fields = ["id","first_name", "last_name", "email"]