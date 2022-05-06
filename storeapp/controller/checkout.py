from django.http import HttpResponse
import random
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
import storeapp
from storeapp.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    rawcart=Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.Product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cartitems:
        total_price=total_price + item.Product.selling_price * item.product_qty

    userprofile=Profile.objects.filter(user=request.user).first()

    context={'cartitems': cartitems ,'total_price':total_price,'userprofile':userprofile}
    return render(request,'storeapp/checkout.html',context)

@login_required(login_url='login')
def placeorder(request):
    if request.method == 'POST':

        currentuser=User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name=request.POST.get('fname')
            currentuser.last_name=request.POST.get('lname')
            currentuser.save()
        if not Profile.objects.filter(user=request.user):
            userprofile=Profile()
            userprofile.user=request.user
            userprofile.phone=request.POST.get('phone')
            userprofile.address=request.POST.get('address')
            userprofile.city=request.POST.get('city')
            userprofile.state=request.POST.get('state')
            userprofile.country=request.POST.get('country')
            userprofile.pincode=request.POST.get('pincode')
            userprofile.save()


        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.lname=request.POST.get('lname')
        neworder.email=request.POST.get('email')
        neworder.phone=request.POST.get('phone')
        neworder.address=request.POST.get('address')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.country=request.POST.get('country')
        neworder.pincode=request.POST.get('pincode')

        neworder.payment_mode=request.POST.get('payment_mode')
        neworder.payment_id=request.POST.get('payment_id')

        cart=Cart.objects.filter(user=request.user)
        cart_total_price= 0
        for item in cart:
            cart_total_price = cart_total_price + item.Product.selling_price *item.product_qty
        neworder.total_price=cart_total_price
        track_no='Deepa'+ str(random.randint(1111111,9999999)) 
        while Order.objects.filter(tracking_no=track_no):
            track_no='Deepa'+ str(random.randint(1111111,9999999)) 


        neworder.tracking_no=track_no
        neworder.save()

        neworderitems=Cart.objects.filter(user=request.user)
        for item in neworderitems:
            orderitem.objects.create(
                order=neworder,
                Product=item.Product,
                price=item.Product.selling_price,
                quantity=item.product_qty
            )

            #to decrease the product quantity from availale stock

            orderproduct=product.objects.filter(id=item.Product_id).first()
            orderproduct.quantity=orderproduct.quantity - item.product_qty
            orderproduct.save()
            
            #To clear users cart
            
            Cart.objects.filter(user=request.user).delete()
           
            pay_mode= request.POST.get('payment_mode')
            if (pay_mode == 'Paid by Razorpay' or pay_mode == 'Paid by paypal' ):
                return JsonResponse({'status':'Your Order has beem placed successfully.... '})

            else:
                 messages.success(request,'Your order has been placed successfully....')
    return redirect('/')

@login_required(login_url='login')
def razorpaycheck (request):
    cart=Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.Product.selling_price * item.product_qty

    return JsonResponse({
        'total_price': total_price
        
        })
def orders(request):
    return HttpResponse("My orders page")


        
        
    
