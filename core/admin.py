from django.contrib import admin
from .models import User, Category, Product, SaleOn

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SaleOn)
