from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from .cart import Cart
from woodmat.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
  cart=Cart(request)
  cart_products=cart.get_prods
  quantities=cart.get_quants
  return render(request,"cart_summary.html",{"cart_products":cart_products, "quantities":quantities})

def cart_add(request):
  #get the cart
  cart=Cart(request)
  #test POST
  if request.POST.get('action')=='post':
    #get stuff
    product_id=int(request.POST.get('product_id'))
    product_qty=int(request.POST.get('product_qty'))

    #lookup product inDB
    product= get_object_or_404(Product,id=product_id)
    #save to session
    cart.add(product=product,quantity=product_qty)

    #get cart quantity
    cart_quantity=cart.__len__()

    #return response
    # response=JsonResponse({'product Name:' :product.name})
    response=JsonResponse({
      'qty:' :cart_quantity,
      'message': 'Product added to cart successfully'

                           })
    
    return response


def cart_delete(request):
  pass

def cart_update(request):
  cart=Cart(request)
  #test POST
  if request.POST.get('action')=='post':
    #get stuff
    product_id=request.POST.get('product_id')
    product_qty=request.POST.get('product_qty')

    cart.update(product=product_id,quantity=product_qty)
    response= JsonResponse({
      'qty':product_qty,
      'message': 'Product updated successfully' 
      })
    return response
 
  
    

  