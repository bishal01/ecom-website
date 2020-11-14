from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib import messages
from .utils import usercart,allfunction
from .forms import createform
from django.contrib.auth import authenticate,login,logout


def register(request):
    form=createform()
    if request.method=="POST":
        form=createform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
            username = form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            messages.success(request,f'account created sucessfully')
            return redirect("login")
    context={'form':form}
    return render(request,"register.html",context)


# Create your views here.
def home(request):
    cookieget=allfunction(request)
    prod=None
    caty=Category.get_all_category()
    cartitems=cookieget['cartitems']
    c_id=request.GET.get('category')
    print(request.GET)
    if c_id:
        prod=products.get_all_products_by_id(c_id)
    else:
     prod=products.objects.all()
    context={
    'prod':prod,
    'caty':caty,
    'cartitems':cartitems
    }

    return render(request,'home.html',context)


def cart(request):

    cookieget=allfunction(request)
    items=cookieget['items']
    order=cookieget['order']
    cartitems=cookieget['cartitems']
    context={'order':order,'cartitems':cartitems,'items':items}
    return render(request,'cart.html',context)


def shippingcard(request):
    cookieget=allfunction(request)
    items=cookieget['items']
    order=cookieget['order']
    cartitems=cookieget['cartitems']
    context={'order':order,'cartitems':cartitems,'items':items}
    return render(request,'shipping.html',context)


def updateitem(request):
    data=json.loads(request.body)
    productid=data['productid']
    action=data['action']
    print('productid',productid)
    print('action',action)
    customer=request.user.customer
    product=products.objects.get(id=productid)
    Order,created=order.objects.get_or_create(customer=customer,complete=False)
    OrderItem,created=orderitem.objects.get_or_create(Order=Order,Products=product)

    if action=='add':
        OrderItem.quantity=(OrderItem.quantity+1)
        if OrderItem.quantity>product.quantity:
            OrderItem.quantity=product.quantity

    elif action=='remove':
        OrderItem.quantity=(OrderItem.quantity-1)
    OrderItem.save()

    if OrderItem.quantity<=0:
        OrderItem.delete()

    return JsonResponse('item was added behenchod',safe=False)

def process_order(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        Order,created=order.objects.get_or_create(customer=customer,complete=False)
        total=float(data['form']['total'])



    else:

        print("NOT logged in")
        name=data['form']['name']
        email=data['form']['email']
        cookieData=usercart(request)
        items=cookieData['items']
        customer,created=Customer.objects.get_or_create(email=email)
        customer.name=name
        customer.save()
        Order=order.objects.create(customer=customer,complete=False)
        for item in items:
            product=products.objects.get(id=item['Products']['id'])
            Orderitem=orderitem.objects.create(
                Products=product,
                Order=Order,
                quantity=item['quantity']
                )



    Order.complete=True
    Order.transaction_id=transaction_id
    Order.save()
    if Order.shipping==True:
            shippingaddress.objects.create(

              customer=customer,
              Order=Order,
              Address=data['ship']['address'],
              city=data['ship']['city'],
              state=data['ship']['state'],




                )





    print('data:',request.body)
    return JsonResponse('item was processed behenchod',safe=False)


def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
          messages.info(request,'username or password is incorrect')

    context={}
    return render(request,"login.html",context)



def logout_page(request):
    logout(request)
    return redirect('login')


def search(request):
    query=request.GET.get('search')
    caty=Category.objects.get(name=query)
    prod=caty.products_set.all()

    return render(request,'search.html',{'prod':prod})

def buynow(request,pk):
   cookieget=allfunction(request)
   order=cookieget['order']
   p=products.objects.get(id=pk)

   return render(request,'buynow.html',{'prod':p})
