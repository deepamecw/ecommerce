from logging import warning
from django.shortcuts import render,redirect
from .models import category,product
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    trending_prod=product.objects.filter(trending=1)
    context={'trending_prod':trending_prod}
    return render(request,'storeapp/index.html',context)

def collection(request):
    Category = category.objects.all()
    context={'category':Category}
    return render(request,'storeapp/collection.html',context)

def collectionview(request,slug):
    if(category.objects.filter(slug=slug,status=0)):
        products=product.objects.filter(category__slug=slug)
        Category=category.objects.filter(slug=slug).first()
        context={'product':products,'category':Category}
        return render(request,'storeapp/products.html',context)
    else:
       messages.warning(request,"no such category.....")
       return redirect("collection")

def productview(request,cate_slug,prod_slug):
    if(category.objects.filter(slug=cate_slug,status=0)):
        if(product.objects.filter(slug=prod_slug,status=0)):
            products=product.objects.filter(slug=prod_slug,status=0).first
            context={'product':products}   
        else:
            messages.error(request,"no such products....")
            return redirect("collection")               
    else:
        messages.error(request,"no such products....")
        return redirect("collection")
    
    return render(request,'storeapp/view.html',context)

def productlistajax(request):
    products=product.objects.filter(status=0).values_list('name',flat=True)
    productlist=list(products)

    return JsonResponse(productlist,safe=False)

def searchproduct(request):
    if request.method=='POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm=="":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            Product=product.objects.filter(name__contains=searchedterm).first()
            if Product:
                return redirect('collection/'+Product.category.slug+'/'+Product.slug)
            else:
                messages.info(request,"No Product Matched Your Search")
                return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))

    
    

    

    