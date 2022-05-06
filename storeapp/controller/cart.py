from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from storeapp.models import *
from django.contrib.auth.decorators import login_required





def addToCart(request):
    if request.method =='POST':
        print("add to cart")
        if request.user.is_authenticated:
            print("auth completed" , request.POST.get('Product_id'))
            prod_id=int(request.POST.get('Product_id'))
            prod_check= product.objects.get(id=prod_id)
            if(prod_check):
                if(Cart.objects.filter(user=request.user.id,Product_id=prod_id)):                                      
                    return JsonResponse({'status':"Product already in cart"})
                else:
                    prod_qty=int(request.POST.get('product_qty'))                    
                    if prod_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user,Product_id=prod_id,product_qty=prod_qty)                        
                        return JsonResponse({"status":"Product added successfully..."})
                    else:            
                        return JsonResponse({"status":"only"+str(prod_check.quantity)+"quantity available"})
            else:
                return JsonResponse({'status':"No such product found"})

        else:
            return JsonResponse({'status':"Login to continue"})

    return("/") 
@login_required(login_url='login')
def viewcart(request):
    
    cart=Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,'storeapp/viewcart.html',context)

def updatecart(request):
    if request.method =='POST':
        prod_id=int(request.POST.get('Product_id'))
        if(Cart.objects.filter(user=request.user,Product_id=prod_id)):
            prod_qty=int(request.POST.get('product_qty'))
            cart=Cart.objects.get(Product_id=prod_id,user=request.user)
            cart.product_qty=prod_qty  
            cart.save()
            return JsonResponse({'status':'Updated successfully..'})
    return redirect('/')
     
def deletecart(request):    
    if request.method =='POST':
        prod_id=int(request.POST.get("Product_id"))
        if(Cart.objects.filter(user=request.user,Product_id=prod_id)):
            cartitem=Cart.objects.get(Product_id=prod_id,user=request.user)
            cartitem.delete()
        return JsonResponse({'status':'Product deleted successfully....'})
        
    return redirect('/')

    
            

           
        

   

        


