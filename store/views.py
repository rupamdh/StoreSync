from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from core.models import *
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def customer_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        Customer.objects.create(
            store=StoreUser.objects.get(id=request.user.id),
            name=name,
            phone=phone,
            address=address
        )
        return redirect('customers')
    return render(request, 'customer-add.html')


@login_required
def customers(request):
    customers = Customer.objects.filter(store_id=request.user.id)
    
    data = {
        'customers' : customers
    }
    return render(request, 'customers.html', data)

@login_required
def customer_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.name = request.POST['name']
        customer.phone = request.POST['phone']
        customer.address = request.POST['address']
        customer.save()
        messages.success(request, 'Customer saved successfully!')
        return redirect('customers')
        

    data = {
        'customer' : customer
    }
    return render(request, 'customer-edit.html', data)


@login_required
def product_add(request):
    if request.method == 'POST':
        Product.objects.create(
            title=request.POST['title'],
            price=request.POST['price']
        )

    return render(request, 'product-add.html')

@login_required
def products(request):
    products = Product.objects.filter(store_id=request.user.id)

    data = {
        'products' : products
    }
    return render(request, 'products.html', data)