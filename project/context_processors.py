from cart.cart import CartSession
from order.forms import OrderForm

def cart(request):
    return {'cart': CartSession(request.session), }

def orderForm(request):
    return {'orderForm': OrderForm }