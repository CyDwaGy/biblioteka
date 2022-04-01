from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book, ItemOrder, Order

def index(request):
    books_list = Book.objects.all()
    context = {'books_list': books_list}
    return render(request, 'main/index.html', context)

def item(request, id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'main/item.html', context)

def additem(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    user = User.objects.get(id=request.user.id)
    item = Book.objects.get(id=id)
    io = ItemOrder(user=user, item=item)
    io.save()
    try:
        order = Order.objects.get(id=request.user.id)
    except Order.DoesNotExist:
        order = Order(user=user)
        order.save()
    finally:
        order.items.add(io)
    return redirect(f'/item/{id}')

def cart(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        items = list(order.items.all())
        full_price = 0
        for item in items:
            full_price += item.item.price
        context = {'order': order, 'full_price': full_price, 'items': items}
        return render(request, 'main/cart.html', context)
    except Order.DoesNotExist:
        return HttpResponse("Twój koszyk jest pusty")

