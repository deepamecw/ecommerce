from django.http import HttpResponse
import random
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from storeapp.models import *
from django.contrib.auth.decorators import login_required


def index(request):
    orders=Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request,'storeapp/orders.html',context)

def vieworder(request,t_no):
    order=Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems=orderitem.objects.filter(order=order)
    context={'order':order,'orderitems':orderitems}
    return render(request, 'storeapp/vieworder.html',context)
