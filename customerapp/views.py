from django.shortcuts import render,redirect
from .models import Customer,Rentbooking,Carbooking,CarSales,CarSalesCus
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from adminapp.models import Rentalcar,Salescar,Carbrand
from datetime import datetime
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url = 'login')
def home(request):
    sales  = Rentbooking.objects.all()
    sales.delete()
    try:
        current_user = request.user
        detail_user = Customer.objects.get(c_user = current_user)
        context={'customer':detail_user,'cust':current_user}
        print(1)
    except:
        current_user = request.user
        print(2)
        context={
            'cust':current_user
            }
    return render(request,'customer/home.html',context)


# Profile

@login_required(login_url = 'login')
def profile(request):   
    try:
        current_user = request.user
        detail_user = Customer.objects.get(c_user = current_user)
        context={'customer':detail_user,'cust':current_user}
        print(1)
        return render(request,'customer/profile.html',context)
    except:
        current_user = request.user
        context={
            'cust':current_user
            }
        print(1)
        return render(request,'customer/profile.html',context)  



@login_required(login_url = 'login')
def edit(request):
    try:
        current_user = request.user
        detail_user = Customer.objects.get(c_user = current_user)
        context={'customer':detail_user,'cust':current_user}
        print(1)
    except:
        current_user = request.user
        print(2)
        context={'cust':current_user}
    return render(request,'customer/editprofile.html',context)


@login_required(login_url = 'login')
def editDetails(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        gender = request.POST['gender']
        city = request.POST['city']
        state = request.POST['state']
        photo = request.FILES.get('photo')
        print(firstname,lastname,username,address,email,phone,address,gender,city,state,photo)
        current_user = request.user
        current_user.first_name = firstname
        current_user.last_name = lastname
        current_user.username = username
        current_user.email = email
        current_user.save()
        try:
            detail_user = Customer.objects.get(c_user=current_user)
            detail_user.phone = phone
            detail_user.address = address
            if gender != None:
                detail_user.gender = gender
            detail_user.city = city
            detail_user.state = state
            print('photo')
            if photo != None:
                detail_user.photo = photo
            detail_user.save() 
            print('success')      
            messages.success(request,"Profile  is Updated")
            return redirect('profile')
        except:
            detail_user = Customer(
                c_user = current_user ,
                phone = phone ,
                address = address,
                gender = gender,
                city = city ,
                state = state , photo = photo 
            )
            detail_user.save()
            messages.success(request,"Profile is Updated")
            return redirect('profile')
    else: 
        return redirect('profile')
    

@login_required(login_url = 'login')
def changePassword(request):
    return render(request,'customer/changepassword.html')

@login_required(login_url = 'login')
def newpassword(request):
    if request.method == 'POST':
        users = authenticate( username = request.user.is_authenticated ,  old_password = request.POST['oldpassword'])
        if users is not None:
            messages.error(request,"'Current Password Enter Mismatch!")
            return redirect('changepassword')
        else:
            new_password = request.POST['newpassword']
            confirm_password = request.POST['confirmpassword']
            try:
                if new_password ==  confirm_password:
                    u = request.user
                    u.set_password(new_password)
                    u.save()
                    messages.success(request,'Password has been changed!,Please Login')
                    print('success')
                    return redirect('profile')
                else:
                    messages.warning(request,'New Password and confirm Password mismatch!')
                    print('Please try again')
                    return redirect('changepassword')
            except:
                messages.error(request,'Password not changed!')
                print('not change')
                return redirect('profile')
    else:
        return redirect('profile')
            

# Rent Car Booking

@login_required(login_url='login')
def rentalcars(request):
    current_user = request.user
    rental_car = Rentalcar.objects.all()
    detail_user = Customer.objects.get(c_user = current_user)
    context = {'cars': rental_car,'cust':current_user,'customer':detail_user}
    return render(request,'customer/rentalcarscus.html',context)

@login_required(login_url='login')
def book(request,i):
    current_user = request.user
    detail_user = Customer.objects.get(c_user = current_user)
    bookings = Rentalcar.objects.get( id = i )
    context = { 'book' : bookings,'cust':current_user,'customer':detail_user }
    return render(request,'customer/rentbooking.html',context)





def create_booking(request,rent_car):
    rental_car = Rentalcar.objects.get( id = rent_car )
    if request.method == 'POST':
        pick_up = request.POST['pick_up']
        drop_off = request.POST['drop_off']
        drop_off_date = datetime.strptime(drop_off, '%Y-%m-%d').date()
        pick_up_date = datetime.strptime(pick_up, '%Y-%m-%d').date()
        
        total_price = rental_car.price * calculate_booking_days(drop_off_date, pick_up_date)

    
        booking = Rentbooking(
            rental_car = rental_car,
            drop_off = drop_off, 
            total_price = total_price,
            )
        booking.save()
        user_id  = request.user
        car_booking = Carbooking.objects.create(user= user_id)
        car_booking.rent_car.add(booking)
        return redirect('bookings')


    return redirect('home')

def calculate_booking_days(drop_off_date,pick_up_date):

    duration = (drop_off_date - pick_up_date).days
    return duration

@login_required(login_url='login')
def myBooking(request):
    current_user = request.user
    detail_user = Customer.objects.get(c_user = current_user)
    try:
        bookings = Carbooking.objects.filter( user = current_user )
        books = []
        total_amount = 0
        
        for booking in bookings:
            books.extend(booking.rent_car.all())

            total_amount += sum(rent_booking.total_price for rent_booking in booking.rent_car.all())
            

        # client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
        currency = 'INR'
        receipt = 'payment_reciept_' + str(current_user.id)
        payment_amount = int(total_amount * 100) 
        if payment_amount < 100:
            payment_amount = 100
        payment = client.order.create({
            'amount' : payment_amount,
            'currency' : currency,
            'receipt' : receipt
           
        })

        for booking_car in bookings:
            booking_car.payment_id = payment['id']
            booking_car.save()

        print(1)
    except Carbooking.DoesNotExist:
        print(2)
        books = []
        total_amount = 0
    context = { 'cust':current_user,
                'customer':detail_user, 
                'books':books, 
                'payment' : payment,
                'total_amount' : payment_amount, 
                }
    return render(request,'customer/cusbooking.html',context)


@csrf_exempt
def payment_success(request):

    if request.method == 'POST':
        razorpay_payment_id = request.POST.get('payment_id')
    
        # client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
        payments = client.order.fetch(razorpay_payment_id)

        # Check if the payment was successful
        if payments.gets('status') == 'paid':
            car_bookings = Carbooking.objects.filter( payment_id = razorpay_payment_id )

            # update payment status
            for car_booking in car_bookings:
                car_booking.payment_status = True
                car_booking.save()
            
            return render(request,'customer/payment/payment_success.html')

    

@login_required(login_url='login')
def deletebooking(request,car_id):
    current_user = request.user
    try:
        my_booking = Carbooking.objects.get( user = current_user, rent_car = car_id )
        my_booking.delete()
        messages.success(request,'Your booking has been deleted ')
        print(1)    
    except:
        messages.error(request, 'The booking does not exist.')
    return redirect('bookings')   


# second car  booking
@login_required(login_url='login')
def salespage(request,):
    current_user = request.user
    detail_user = Customer.objects.get(c_user = current_user)
    sale_car = Salescar.objects.all()
    context = {'cars' : sale_car,'cust':current_user,'customer':detail_user}
    return render(request,'customer/salescus.html',context)

def sales_Booking(request,i):
    current_user = request.user
    detail_user = Customer.objects.get( c_user = current_user )
    sales_booking = Salescar.objects.get( id = i )
    context = {
        'cust' : current_user,
        'customer' : detail_user,
        'book' : sales_booking
    }
    return render(request, 'customer/used-car-bookiong.html',context)


def create_sales_booking(request,sales_car_id):
    sales_car_details = Salescar.objects.get( id = sales_car_id )
    total_price = sales_car_details.price
    if request.method == 'POST':
        booking_date = request.POST['booking_date']
        confirm_date = request.POST['confirm_date']

        sales_car_booking = CarSalesCus(
            car = sales_car_details,
            booking_date = booking_date,
            confirm_date = confirm_date,
            total_price = total_price 
        )
    
        sales_car_booking.save()
        user_id  = request.user
        car_booking = CarSales.objects.create(user= user_id)
        car_booking.sales_Car.add(sales_car_booking)
        
        messages.success(request,'Second Hand Car Booking are Submitted')

        return redirect('sales')


    
    return redirect('home')


def salesbookingcar(request):
    current_user = request.user
    detail_user = Customer.objects.get(c_user = current_user)
    try:
        sale_booking = CarSales.objects.filter( user = current_user )
        books = []
        
        for booking in sale_booking:
            books.extend(booking.sales_Car.all())
        context = {'cars': books, 'cust': current_user, 'customer': detail_user}
        return render(request, 'customer/salesbooking.html', context)
    except:
        pass
    print(1)
    context = {
        'cust':current_user,
        'customer':detail_user
    }
    return render(request,'customer/salesbooking.html',context)



@login_required(login_url='login')
def deletesalesbooking(request,sale_id):
    current_user = request.user
    try:
        second_car_sale = CarSales.objects.get( user = current_user, sales_Car = sale_id )
        sales_cars = second_car_sale.sales_Car.all()


        for sales_car in sales_cars:
            sales_car.delete()

        second_car_sale.delete()
        messages.success(request,'Your  booking has been deleted')

    except:
        messages.success(request,'Sales booking does not exist')
    return redirect('sales')

def model_filter_car(request,car_brand_id):
    rent_car_brand_name = Carbrand.objects.get( id = car_brand_id )
    rent_car_brand = Rentalcar.objects.filter( car_model__brands =  rent_car_brand_name  )
    context = {
         'car_brand' : rent_car_brand
        }
    return render(request,'customer/searchsalescar.html',context)

# Confirm Payment


def confirm_payment(request,booking_id):
    rent_car_booking = Carbooking.objects.get( id = booking_id )
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    amount_in_paise = rent_car_booking.rent_car.total_price * 100

    try:
        razorpay_order = client.order.create({
            'amount' : amount_in_paise,
            'currency' : 'INR',
            'reciept' : f'rent_car_booking-{ rent_car_booking.id }',
            'notes' :  {
                'booking_id' : rent_car_booking.id,
                'user_id' : rent_car_booking.user.id,
            }
        })
    except Exception as e :
        return render(request, 'customer/payment/error.html', {'error': str(e)})
    context = {
        'booking' : rent_car_booking,
        'razorpay_order_id' : razorpay_order['id'],
        'razorpay_key_id' : settings.RAZORPAY_KEY_ID
    }
    return render(request,'customer/payment/payment.html',context)




@login_required(login_url='login')
def payment_failed(request):
    return render(request,'customer/payment/payment_failed.html')


