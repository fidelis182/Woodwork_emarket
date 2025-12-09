class Cart():
  def __init__(self,request):
    self.session= request.session

    #get current session key if it exists
    cart=self.session.get('session_key')

    #if the user is new then no session key,create one
    if 'session_key' not in request.session:
      cart=self.session['session_key']={}

    #make sure cart is available to all pages
    self.cart=cart


  