from django.shortcuts import render
from .models import Producers, Categories, Products



def main_view(request):
    category = Categories.objects.all()
    data = {'category': category}
    return render(request, 'main.html', data)

def category(request,id):
    category_user = Categories.objects.get(pk=id)
    category_product = Products.objects.filter(category=category_user)
    category = Categories.objects.all()
    data = {'category_user':  category_user,'category_product':category_product , 'category':category }
    return render(request, 'category_product.html', data)

def product(request,id):
    product_user = Products.objects.get(pk=id)
    category = Categories.objects.all()
    data = {'product_user': product_user, 'category': category}
    return render(request, 'product.html', data)

