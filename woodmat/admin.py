from django.contrib import admin

from woodmat.models import Category, Customer, Order, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)