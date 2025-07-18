from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')

@login_required(login_url='loginpage')
def about(request):
            #if request.user.is_authenticated:
                return render (request,'about.html')
            #else:
                 #return render(request,'login.html')
        #if 'uid' in request.session:
           # return render(request,'about.html')
        #else:

            #return render(request,'about.html')    
            #return render(request,'login.html')
   
def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['name1']
        last_name=request.POST['name2']
        username=request.POST['name3']
        password=request.POST['pass1']
        cpassword=request.POST['pass2']
        email=request.POST['email1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists!!!!")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email )
                user.save()

        else:
            messages.info(request,"Password Doesnot Match!!!!")
            return redirect('signup')
        return redirect('loginpage')
    return render(request,'signup.html')


def login1(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pass1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('adminhome')
            else:
                 
                 
                 
           # request.session['uid']=user.id
          
            
                auth.login(request,user)
                messages.info(request,f'welcome  {username} you have been logged in!!')
                return redirect('about')
        else:
            messages.info(request,"invalid username or password!!!!")
            return redirect('loginpage')
    else:
        return render(request,"login.html")  

@login_required(login_url='loginpage')
def logout(request):
   # request.session['uid']= ""
   #if request.user.is_authenticated:
        auth.logout(request)
        return redirect('home')    

def adminhome(request):
     return render(request,'admin.html')