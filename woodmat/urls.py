from django.contrib import admin
from django.urls import path,include

from woodmat import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('categories/', views.categories, name="categories"),
    path('category_detail/', views.category_detail, name="category_detail"),
    path('product_detail/', views.product_detail, name="product_detail"),
    path('products/', views.products, name="products"),
    path('artisan_profile/', views.artisan_profile ,name= "artisan_profile")
    
]