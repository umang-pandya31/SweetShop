from django.shortcuts import render,redirect,get_object_or_404
from model.models import *
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages


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

    #For Sorting
    sort = request.GET.get('sort')

    # Apply sorting based on the selected option
    if sort == 'name_asc':
        sweets = sweets.order_by('name')
    elif sort == 'name_desc':
        sweets = sweets.order_by('-name')
    elif sort == 'price_asc':
        sweets = sweets.order_by('price')
    elif sort == 'price_desc':
        sweets = sweets.order_by('-price')
    elif sort == 'quantity_asc':
        sweets = sweets.order_by('quantity')
    elif sort == 'quantity_desc':
        sweets = sweets.order_by('-quantity')
    return render(request, 'index.html', {'sweets': sweets})

    # sweets = Sweet.objects.all()
    # return render(request,"index.html",{'sweets': sweets})

#for add sweet easily get data with post method and with the use of Object save in database.
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


# with use of pk variable update the value and then update i database
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

def purchase_sweet(request):
    if request.method == "POST":
        sweet_id = request.POST.get("sweet_id")
        amount = int(request.POST.get("amount"))
        #this is very helpfull, if Sweet is found then return this if not then return 404.
        sweet = get_object_or_404(Sweet, id=sweet_id) 

        try:
            sweet.purchase(amount)  #alredy purchase method define in model class so  direct use it.
            messages.success(request, f"Purchased {amount} successfully!")
        except ValueError as e:
            messages.error(request, str(e))

    return redirect('/', sweet_id=sweet_id)  # Redirect to home page

def add_stock(request):
    if request.method == 'POST':
        sweet_id = request.POST.get('sweet_id')
        amount = int(request.POST.get('amount', 0))
        sweet = get_object_or_404(Sweet, id=sweet_id)

        if amount > 0:
            sweet.restock(amount)  # restock method is alredy define in model.
            messages.success(request, f'Added {amount} items to stock of {sweet.name}.')
        else:
            messages.error(request, 'Invalid amount.')

    return redirect('/')  # redirect home page
