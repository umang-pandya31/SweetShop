from django.shortcuts import render,redirect
from model.models import *
from django.http import HttpResponse

def index(request):
    sweets = Sweet.objects.all()
    return render(request,"index.html",{'sweets': sweets})

def add_sweet(request):
    if request.method == "POST":
        name=request.POST['name']
        category=request.POST['category']
        price=request.POST['price']
        quantity=request.POST['quantity']
        Sweet(name=name,category=category,price=price,quantity=quantity).save()
        return redirect("/")

    return render(request,"add_sweet.html")
