from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, Http404
from .models import Product
# Create your views here.

def index(request):
    lasted_product = Product.objects.order_by('-created_date')[:12]
    context ={
        'lasted_product' : lasted_product
    }
    return render(request, "products/index.html", context)
    
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/detail.html", {'product': product})
    
