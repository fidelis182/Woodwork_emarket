from django.shortcuts import get_object_or_404, render
from .cart import Cart
from woodmat.models import Product
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
  return render(request,"cart_summary.html")

def cart_add(request):
  #get the cart
  cart=Cart(request)
  #test POST
  if request.POST.get('action')=='post':
    #get stuff
    product_id=int(request.POST.get('product_id'))
    #lookup product inDB
    product= get_object_or_404(Product,id=product_id)
    #save to session
    cart.add(product=product)

    #return response
    response=JsonResponse({'product Name':product.name})
    return response


def cart_delete(request):
  pass

def cart_update(request):
  pass