from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()

    new_query = query_set.filter(title__contains="car")
    for product in new_query:
        print(product)

    return render(request, 'hello.html', {'name': 'Mosh'})
