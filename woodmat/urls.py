from django.contrib import admin
from django.urls import path,include
from woodmat import views


urlpatterns = [
    path('', views.index, name="index"),
    path('category/<str:foo>/', views.category, name='category'),
    path('category_detail/', views.category_detail, name="category_detail"),
    path('product_detail/<int:pk>/', views.product_detail, name="product_detail"),
    path('products/', views.products, name="products"),
    path('artisan_profile/', views.artisan_profile ,name= "artisan_profile"),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name ='register'),
    
]