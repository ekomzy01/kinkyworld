from django.contrib import admin
from .models import Products, Customer, Order, OrderItem,ShippingAddress

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Products, ProductAdmin)

admin.site.register(Customer)
# admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)