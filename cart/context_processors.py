from .cart import Cart

#create context processor to make sure sure cart works on all pages
def cart(request):
  #return default data
  return{'cart':Cart(request)}