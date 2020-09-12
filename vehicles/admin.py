from django.contrib import admin
from .models import Vehicle

# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['owner', 'vehicle_model', 'doc_number']
    search_fields = ['owner', 'vehicle_model', 'doc_number']


admin.site.register(Vehicle, VehicleAdmin)
