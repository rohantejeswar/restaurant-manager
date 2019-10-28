from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Menu

def index_view(request):
    return render(request, "home/index.html", {})

def menu_view(request):
    menus = Menu.objects.order_by('category')
    categories = ['Starters', 'Main Course', 'Bevrages', 'Desserts']
    numbers = [0,1,2,3]
    context = {
        'menus': menus,
        'categories': categories,
        'nums': numbers,
    }
    return render(request, "home/menu.html", context)

''' backup
def menu_view(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus 
    }
    return render(request, "home/menu.html", context)
'''

def cart_view(request):
    try:
        ids_str = request.GET.get('id')
        ids = ids_str.split(',')

        items = Menu.objects.filter(pk__in=ids)
        context = {'ids': ids, 'items': items}
        return render(request, 'home/cart.html', context)
    except Exception as e:
        return HttpResponse(e)