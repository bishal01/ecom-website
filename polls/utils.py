import json
from .models import *


def usercart(request):
        try:
            cart=json.loads(request.COOKIES['cart'])

        except:
         cart={}
        print(cart)
        items=[]
        Order={'shipping':False,'get_cart_items':0,'total_price':0}
        cartitems=Order['get_cart_items']
        for i in cart:
            try:
              cartitems+=cart[i]['quantity']
              prod=products.objects.get(id=i)
              total=prod.price*cart[i]['quantity']
              Order['total_price']+=total
              Order['get_cart_items']+=cart[i]['quantity']
              item={
              'Products':{
              'id':prod.id,
              'name':prod.name,
              'price':prod.price,
              'image':prod.image

              },
              'quantity':cart[i]['quantity'],
              'get_total':total
              }
              items.append(item)
              if prod.digital==False:
                Order['shipping']=True
              else:
                Order['shipping']=False




            except:
                pass
        return {'cartitems':cartitems,'order':Order,'items':items}



def allfunction(request):
    if request.user.is_authenticated:
      customer=request.user.customer
      Order,created=order.objects.get_or_create(customer=customer,complete=False)
      items=Order.orderitem_set.all()
      cartitems=Order.get_cart_items
    else:
        cookieget=usercart(request)
        items=cookieget['items']
        Order=cookieget['order']
        cartitems=cookieget['cartitems']


    return {'cartitems':cartitems,'order':Order,'items':items}

