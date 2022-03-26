from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

def index(request):
    Books_list = Book.objects.all()
    context = {'Books_list': Books_list}
    return render(request, 'main/index.html', context)
