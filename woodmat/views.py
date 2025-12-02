from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,'index.html')


def categories(request):
  return render(request,'categories.html')

def category_detail(request):
  return render(request,'category_detail.html')

def products(request):
  return render(request,'products.html')

def product_detail(request):
  return render(request,'product_detail.html')



