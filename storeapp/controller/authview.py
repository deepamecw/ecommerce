from django.shortcuts import render,redirect
from django.contrib import messages

from storeapp.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout



def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST) 
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,' Account was created for  ' + user)
            return redirect('/login')
    
    context = {'form':form}
    return render(request,'auth/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"you are already logged in!..")
        return redirect('/')
    else:
        if request.method == "POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"logged in successfully...")
                return redirect("/")
            else:
                messages.error(request,"invalid username or password")
                return redirect('/login')
                
    return render(request,'auth/login.html')
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out successfully...")
    return redirect('/')
        