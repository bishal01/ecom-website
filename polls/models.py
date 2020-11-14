from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.db.models.signals import post_save
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.user)

class order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    complete = models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=200,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)


    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.Products.digital==False:
                shipping=True
        return shipping

    @property
    def total_price(self):
        orderitem=self.orderitem_set.all()
        total=sum([i.get_total for i in orderitem])
        return total






    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class Category(models.Model):
    name=models.CharField(max_length=20,default="")

    @staticmethod
    def get_all_category():
        return Category.objects.all()
    def __str__(self):
            return self.name



class products(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    image=models.ImageField(null=True,blank=True)
    digital=models.BooleanField(default=False,null=True,blank=True)
    quantity=models.IntegerField(default=6,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    @staticmethod
    def get_all_products_by_id(category_pass):
       if category_pass:
        return products.objects.filter(category=category_pass)
       else:
        return products.objects.all()




class orderitem(models.Model):
    Products=models.ForeignKey(products,on_delete=models.SET_NULL,null=True)
    Order=models.ForeignKey(order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)


    @property
    def get_total(self):
        total=self.Products.price*self.quantity
        return total


class shippingaddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    Order=models.ForeignKey(order,on_delete=models.SET_NULL,null=True,blank=True)
    Address=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Address


def save_profile(sender, instance, created, **kwargs):
    user=instance
    if created:
        Customer.objects.create(user=user)
        print("profile created")

post_save.connect(save_profile,sender=User)





