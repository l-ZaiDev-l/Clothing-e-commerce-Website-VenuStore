from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    return render(request,'products/product.html',{'pro':Product.objects.get(name='iphone_12')}) # id =1425

def products(request):
    return render(request,'products/products.html',{'pro':Product.objects.all()})
    # or {'pro':Product.objects.Filter(price=100)}
