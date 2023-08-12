from django.contrib import admin
from .models import Product, Customer, Cell


@admin.action(description='Обнулить количество товара')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count_prod=0)


class ProductAdmin(admin.ModelAdmin):
    """Список товаров"""
    list_display = ['name_prod', 'price', 'count_prod']
    ordering = ['name_prod', 'count_prod']
    list_filter = ['date_added']
    search_fields = ['description']
    search_help_text = 'Поиск по описанию'
    actions = [reset_quantity]

    readonly_fields = ['date_added', 'price']


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Cell)
