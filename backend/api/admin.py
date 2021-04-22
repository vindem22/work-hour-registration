from django.contrib import admin
from api.models import Employee, Record
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [ "id","first_name", "last_name"]
    search_fields = ["first_name", "last_name", "email"]

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = [ "employee", "arrive_time",'exit_time']
    search_fields = [ "employee_id", "arrive_time",'exit_time']