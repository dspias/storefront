from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(query_set)})
