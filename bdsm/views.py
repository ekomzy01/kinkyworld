from django.shortcuts import render
from products.utils import cookieCart, cartData, guestOrder
from products.models import Products


def home(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Products.objects.all()
    context = {'products':products, 'cartItems':cartItems, 'items':items, 'order':order}
    return render(request, 'home.html', context)