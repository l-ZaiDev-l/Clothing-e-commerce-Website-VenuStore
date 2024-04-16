from django.contrib import admin
from .models import Product # importe products
from .models import Teste # importe products

# Register your models here.

admin.site.register(Product)

admin.site.register(Teste)


