from django.contrib import admin

# Register your models here.
from shop_unit.models import ShopUnit


class ShopUnitAdmin(admin.ModelAdmin):
    list_display = ["id", "parentId", "type", "name", "price", "date"]
    readonly_fields = ["date"]


admin.site.register(ShopUnit, ShopUnitAdmin)