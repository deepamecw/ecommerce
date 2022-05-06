from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
import storeapp
from storeapp.models import *
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def index(request):
    WishList= wishlist.objects.filter(user=request.user)
    context={'WishList': WishList}
    return render(request,'storeapp/wishList.html',context)
    
def addtowishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('Product_id'))
            product_check=product.objects.get(id=prod_id)
            if(product_check):
                if(wishlist.objects.filter(Product_id=prod_id,user=request.user)):
                    
                    return JsonResponse({'status':"Product already in wishlist"})
                else:
                    wishlist.objects.create(user=request.user,Product_id=prod_id)
                    return JsonResponse({'status':"Product added to wishlist"})
            else:
                 return JsonResponse({'status':"No such product found"})
       
        return JsonResponse({'status':"Login to continue..."    })
    return redirect('/')
def deletewishlist(request):
    if request.method =='POST':
        if request.user.is_authenticated:
           prod_id=int(request.POST.get('Product_id'))
           if(wishlist.objects.filter(Product_id=prod_id,user=request.user)):
               wishlistitem=wishlist.objects.get(Product_id=prod_id)
               wishlistitem.delete()
               return JsonResponse({'status':"Product removed from wishlist"})
           else:
                wishlist.objects.create(user=request.user,Product_id=prod_id)
                return JsonResponse({'status':"Product not found.."})

        else:
            return JsonResponse({'status':"Login to continue...."})
    return redirect('/')
        
    

           

        



    

