from django.contrib import admin
from .models import Product, Variation, ReviewRating
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','fecha_modificacion', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
