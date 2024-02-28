from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .decorators import *
from .models import *
# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            pass
    return render(request, 'login.html')

def admin_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def home_page(request):
    return render(request, 'index.html')


@login_required
@is_superadmin
def add_store(request):
    if request.method == 'POST':
        store_name = request.POST['store_name']
        phone = request.POST['phone']
        password = request.POST['password']
        
        StoreUser.objects.create_user(
            store_name = store_name,
            phone = phone,
            password = password
        )


    return render(request, 'store-add.html')

@login_required
@is_superadmin
def all_stores(request):
    stores = StoreUser.objects.all().exclude(is_superuser=True)
    
    data = {
        'stores' : stores
    }

    return render(request, 'stores.html', data)