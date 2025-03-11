from django.shortcuts import render
from .models import *
from .models import OrderItem


from django.http import JsonResponse
import json


# Create your views here.
def store(request):

    if request.user.is_authenticated:
        curses=request.user.customer
        order,created = Order.objects.get_or_create(customer=curses,complete=False)
        items=order.orderitem_set.all()
        cart_items=order.get_cart_items
    else:
        items=[]
        order={'get_cart_items':0,'get_cart_total':0,'shipping':False}
        cart_items=order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products,'cart_items': cart_items,'items':items }
    return render(request, 'store/store.html',context)  # Only specify the relative path

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order={"get_cart_total":0,"get_cart_items":0,'shipping':False}
        cart_items = order['get_cart_items']

    context = {'items': items,'order':order,'cart_items':cart_items}

    return render(request, 'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0,'shipping':False}
        cart_items = order['get_cart_items']
    context = {'items': items, 'order': order,'cart_items':cart_items}
    return render(request, 'store/checkout.html',context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action, 'ProductId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        order_item.quantity += 1
        order_item.save()

    elif action == "remove":
        if order_item.quantity <= 1:
            order_item.delete()
            return JsonResponse({'message': 'Item removed from cart'}, safe=False)  # Return early after deletion
        else:
            order_item.quantity -= 1
            order_item.save()  # Save only if not deleting

    return JsonResponse({'message': 'Item updated successfully'}, safe=False)
