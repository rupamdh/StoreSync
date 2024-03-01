"""
URL configuration for sms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
from store.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', admin_login, name='login'),
    path('logout/', admin_logout, name='logout'),

    path('stores/add/', add_store, name='store-add'),
    path('stores/', all_stores, name='stores'),

    path('customers/add/', customer_add, name='customer-add'),
    path('customers/edit/<int:id>/', customer_edit, name='customer-edit'),
    path('customers/', customers, name='customers'),

    path('products/add/', product_add, name='product-add'),
    path('products/edit/<int:id>/', products_edit, name='product-edit'),
    path('products/', products, name='products'),
]
