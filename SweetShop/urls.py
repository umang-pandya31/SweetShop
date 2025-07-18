"""
URL configuration for SweetShop project.

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
from SweetShop import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("",views.index,name="index"),
    path("add_sweet",views.add_sweet),
    path("delete_sweet/<int:key>", views.delete_sweet, name="delete_sweet"), # pass key for get id of sweet with url
    path('update_sweet/<int:pk>/', views.update_sweet, name='update_sweet'),  # pass pk for get id of sweet with url
    path('purchase_sweet', views.purchase_sweet, name='purchase_sweet'),
    path('add_stock', views.add_stock, name='add_stock'),

    

]
