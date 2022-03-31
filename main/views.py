from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

def index(request):
    Books_list = Book.objects.all()
    context = {'Books_list': Books_list}
    return render(request, 'main/index.html', context)

def item(request, id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'main/item.html', context)