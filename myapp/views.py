from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
    return render(request,'index.html')

def loginPage(request):
    return render(request,'auth/login.html')

def signUpPage(request):
    return render(request,'auth/register.html')

def forgotPassword(request):
    return render(request,'auth/forgotpassword.html')

def resetPassword(request):
    return render(request,'auth/resetpassword.html')

def signUp(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        print(first_name,last_name,username,email)
        if User.objects.filter(username = username):
            print('User Exists')
            return redirect('register')
        else:
            pass_word = request.POST['password']
            c_password = request.POST['confirm_password']
            if pass_word == c_password:
                if User.objects.filter(username = username):    
                    return redirect('index')
                else:
                    user = User.objects.create_user(
                        first_name = first_name,
                        last_name = last_name,
                        username = username,
                        email = email,
                        password = pass_word
                    )
                    user.save()
                    print('Success')
                    messages.success(request,"Register request submitted successfully. ")
                    subject = 'Welcome to BANDIT Online Car Booking'
                    message = f'{ username }, You are successfully Registered!!   '
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [settings.EMAIL_HOST_USER,]
                    send_mail(subject,message,email_from,recipient_list)
                    return redirect('login')
            else:
                messages.error(request,"Invalid password please try again")
                print('Password is no matching')
                return redirect('register')
    else:
        return redirect('index')
    
def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username , password = password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                messages.success(request,"WELCOME ADMIN")
                return redirect('adminhome')
            else:
                login(request,user)
                auth.login(request,user)
                messages.success(request,f"Welcome {username} to Bandit Online Car Booking")
                return redirect('home')
        else:
            messages.error(request,'Invalid User Name or Password. Please check again!!!!!!')
            return redirect('login')
    else:
        return redirect('index')
    
def signOut(request):
    logout(request)
    messages.success(request,"Thank you for visit BANDIT")
    print('logout success')
    return redirect('index')
