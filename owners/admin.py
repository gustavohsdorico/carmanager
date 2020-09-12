from django.contrib import admin
from .models import Owner
from vehicles.models import Vehicle


# Register your models here.


class VehiclesInLine(admin.TabularInline):
    model = Vehicle
    verbose_name = "Veiculo do proprietário"
    verbose_name_plural = "Veiculos do proprietário"
    extra = 1


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email']
    inlines = [VehiclesInLine]
    search_fields = ['name', 'phone_number', 'email']


admin.site.register(Owner, OwnerAdmin)
