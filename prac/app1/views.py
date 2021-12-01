from django.http import request
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import customform, settingform ,UserProfileForm , picForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from .models import UserProfile,Comment
from .models import ItemListed
from django.contrib.auth.models import User
from django.core import serializers
from .models import UserProfile , cart

def create_user(request):
    torm = customform()
    if request.method =='POST':
        torm = customform(request.POST)
        if torm.is_valid():
            torm.save()
            user = User.objects.get(username = request.POST['username'])
            dorm = UserProfile(user = user)
            dorm.save()
            return redirect('/login/')
    
    ctx = {'form':torm}
    return render(request , 'app1/signup.html',ctx)
# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username , password = password)
        if user is not None:
            login(request ,user)
            return redirect('/home/')
    return render(request , 'app1/login.html')

@login_required(login_url='/login/')
def home(request):
    data = ItemListed.objects.all()
    currentuser = request.user
    cart_count = cart.objects.filter(user=request.user).count()
    ctx = {
        'user':currentuser,
        'UserProfile':UserProfile,
        'item':data,
        'cart_count':cart_count
    }
    return render(request, 'app1/home.html',ctx)

@login_required(login_url='/login/')
def setting_view(request):
    torm = settingform()
    dorm = UserProfileForm()
    pic = picForm()
    if request.method == 'POST':
        torm = settingform(request.POST , instance=request.user)
        if torm.is_valid():
            torm.save()
    
    userdata = User.objects.get(pk = request.user.id)
    ctx = {
            'setting':torm,
            'userdata':userdata,
            'userprofile':dorm,
            'pic':pic,
        }
    return render(request , 'app1/setting.html',ctx)

@login_required(login_url='/login/')
def general(request):
    data = {
        'xml':'Poka Radi'
    }
    return JsonResponse(data)


@login_required(login_url='/login/')
def usersentdata(request):
    if request.method=='POST':
        data = UserProfileForm(request.POST,instance=request.user.userprofile)
        if data.is_valid():
            data.save()
            redirect('/setting/')
        
    return redirect('/setting/')

@login_required(login_url='/login/')
def passwordvalidation(request):
    if request.method =="POST":
        user = User.objects.get(id = request.user.id)
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        if pwd1 == pwd2:
            user.set_password(pwd1)
            user.save()
    return redirect('/setting/')

@login_required(login_url='/login/')
def addtocart(request):
    if request.method == 'GET':
        data = request.GET['data']
        cart_item = ItemListed.objects.get(id=data)
        try:
            cart_data = cart.objects.get(user=request.user , item = cart_item)
            cart_data.quantity = cart_data.quantity +1
            cart_data.save()
            length = cart.objects.filter(user=request.user).count()
            return JsonResponse(length , safe=False)
        except:
            cart_data = cart(user=request.user , item = cart_item , quantity = 1)
            cart_data.save()
            length = cart.objects.filter(user=request.user).count()
            return JsonResponse(length , safe=False)
    else:
        return JsonResponse('unsuccessful',safe=False)
    

@login_required(login_url='/login/')
def cartshow(request):
    cart_data = cart.objects.filter(user = request.user)
    ctx = {
        'data':cart_data,
    }
    return render(request , 'app1/cart.html',ctx)

@login_required(login_url='/login/')
def qntcng(request):
    if request.method=="GET":
        data = request.GET['data']
        idofdata = request.GET['id']
        ItemObject = ItemListed.objects.get(id=idofdata)
        cart_item = cart.objects.get(user=request.user ,item=ItemObject )
        if data == '-':
            if cart_item.quantity <= 1:
                cart_item.delete()
                return JsonResponse('delete', safe=False)
            else:
                cart_item.quantity -= 1
                cart_item.save()
                return JsonResponse(cart_item.quantity ,safe=False)
        elif data =='+':
            cart_item.quantity +=1
            cart_item.save()
            return JsonResponse(cart_item.quantity ,safe=False)
            

@login_required(login_url='/login/')
def bigpicview(request, id):
    Item_view = ItemListed.objects.get(id=id)
    cart_item = cart.objects.filter(user=request.user).count()
    print(cart_item)
    ctx = {
        'items':Item_view,
        'num':cart_item,
    }
    return render(request , 'app1/bigview.html' ,ctx)

@login_required(login_url='/login/')
def imagechange(request):
    if request.method == "GET":
        changepic = picForm(request.GET , request.FILES , instance=request.user)
        if changepic.is_valid():
            changepic.save()
        else:
            print('hi')
        return redirect('/setting/')
    
