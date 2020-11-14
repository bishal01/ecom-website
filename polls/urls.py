from django.urls import path
from . import views


urlpatterns=[
path('',views.home,name="home" ),
path('cart/',views.cart,name="cart" ),
path('update',views.updateitem,name='update'),
path('shipping/',views.shippingcard,name="shipping"),
path('process/',views.process_order,name="process"),
path('register/',views.register,name="register"),
path('login/',views.loginuser,name="login"),
path('logout/',views.logout_page,name="logout"),
path('search/',views.search,name="search"),
path('buy/<str:pk>/',views.buynow,name="buynow")



]
