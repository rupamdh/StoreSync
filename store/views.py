from django.shortcuts import render, redirect
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