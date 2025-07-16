from django.shortcuts import render,redirect,get_object_or_404
from model.models import *
from django.http import HttpResponse
from django.db.models import Q

def index(request):
    from django.db.models import Q

def index(request):
    sweets = Sweet.objects.all()
    query = request.GET.get('query')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if query:
        sweets = sweets.filter(
            Q(name__icontains=query) |
            Q(category__icontains=query)
        )
    if min_price:
        sweets = sweets.filter(price__gte=min_price)  #__gte is predefine function meand greterthan equal to
    if max_price:
        sweets = sweets.filter(price__lte=max_price)  #__lte is predefine function meand lessthan equal to

    return render(request, 'index.html', {'sweets': sweets})

    # sweets = Sweet.objects.all()
    # return render(request,"index.html",{'sweets': sweets})

def add_sweet(request):
    if request.method == "POST":
        name=request.POST['name']
        category=request.POST['category']
        price=request.POST['price']
        quantity=request.POST['quantity']
        Sweet(name=name,category=category,price=price,quantity=quantity).save()
        return redirect("/")

    return render(request,"add_sweet.html")

#for delete sweets and direct redirect to home page
def delete_sweet(request,key):
    sweet = get_object_or_404(Sweet, id=key)
    if request.method == 'POST':
        sweet.delete()
        return redirect('/')
    
    return render(request, 'sweets/confirm_delete.html', {'sweet': sweet})


def update_sweet(request, pk):
    sweet = get_object_or_404(Sweet, pk=pk)

    if request.method == 'POST':
        sweet.name = request.POST.get('name')
        sweet.category = request.POST.get('category')
        sweet.price = request.POST.get('price')
        sweet.quantity = request.POST.get('quantity')

        sweet.save()
        return redirect('/')

    return render(request, 'update_sweet.html', {'sweet': sweet,'edit': True})