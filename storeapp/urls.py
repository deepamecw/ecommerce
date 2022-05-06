from django.urls import path
from . import views
from storeapp.controller import authview,cart,wishList,checkout,order



urlpatterns = [
    path('',views.home,name = 'home'),
    path('collection',views.collection,name='collection'),
    path('collection/<str:slug>',views.collectionview,name='collectionview'),
    path('collection/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'), 
    path('product-list',views.productlistajax),
    path('searchproduct',views.searchproduct,name="searchproduct"),

    path('register',authview.register,name="register"),
    path('login',authview.loginpage,name='login'),
    path('logout',authview.logoutpage,name="logout"),
    path('add-to-cart',cart.addToCart,name="addtocart"),
    path('viewcart',cart.viewcart,name="viewcart"),
    path('update-cart',cart.updatecart,name="updatecart"),
    path('delete-cart',cart.deletecart,name="deletecart"),

    path('WishList',wishList.index,name="WishList"),
    path('add-wishlist',wishList.addtowishlist,name="add-wishlist"),
    path('delete-wishlist',wishList.deletewishlist,name='deletewishlist'),

    path('checkout',checkout.index,name='checkout'),
    path('place-order',checkout.placeorder,name='placeorder'),
    path('proceed-to-pay',checkout.razorpaycheck),
    path('my-orders',order.index,name="myorders"),
    path('view-order/<str:t_no>',order.vieworder,name='vieworder')
   

    


    


    


]   

    
    

