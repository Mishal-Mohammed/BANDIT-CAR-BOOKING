from django.shortcuts import render,redirect
from customerapp.models import Customer
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Carbrand,Carmodel,Rentalcar,Salescar
from django.contrib import messages
from customerapp.models import Carbooking,Salescar,CarSales

# Create your views here.
@login_required( login_url= 'login' )
def home(request):
    cur = request.user
    cu = {'admin':cur}
    return render(request,'admin/home.html',cu)

@login_required( login_url= 'login' )
def userDetail(request):
    detail_user = Customer.objects.all()
    context = { 'customers' : detail_user}
    return render(request,'admin/userDetails.html',context)

@login_required( login_url= 'login' )
def carBrand(request):
    brand = Carbrand.objects.all()
    models = Carmodel.objects.all()
    context = { 'brand': brand,'models': models }
    return render(request,'admin/brandDetails.html',context)

@login_required( login_url= 'login' )
def addBrand(request):
    if request.method == 'POST':
        brand_name = request.POST['brand']
        new_brand = Carbrand( brand = brand_name )
        new_brand.save()
        messages.success(request,'Brand Name added')
        return redirect('carbrand')
    
@login_required( login_url= 'login' )
def addModel(request):
    if request.method == 'POST':
        model_name = request.POST['model']
        brand_id = request.POST['brand']
        brand_name = Carbrand.objects.get( id = brand_id )
        new_model = Carmodel( brands = brand_name, models = model_name )
        new_model.save()
        print("Success Model create")
        messages.success(request,'Car Model added')
        return redirect('carbrand')
    
@login_required( login_url= 'login' )
def deletemodels(request,model_id):
    model_name = Carmodel.objects.get( id = model_id )
    model_name.delete()
    messages.success(request,"Car model has been deleted")
    return redirect('carbrand')
    
# rental views

@login_required( login_url= 'login' )
def rentalCars(request):
    rental_cars = Rentalcar.objects.all()
    context = {'cars':rental_cars}
    return render(request,'admin/rentalcars.html',context)

@login_required( login_url= 'login' )
def addRentalCars(request):
    global brands
    brands = Carbrand.objects.all()
    context = {'brand':brands}
    return render(request,'admin/addrentcar.html',context)

@login_required( login_url= 'login' )
def model_filter(request,i):
    global b
    b=Carbrand.objects.get(id=i)
    modelss=Carmodel.objects.filter(brands=b)
    dicst = {'models':modelss}
    return render(request,'admin/addrentcar.html',dicst)

@login_required( login_url= 'login' )
def addrentalcar(request):
    if request.method == 'POST':
        a_models = request.POST['model']
        new_model = Carmodel.objects.get( id = a_models )
        a_fuel = request.POST['fuel']
        a_kilometers = request.POST['kilometers']
        a_description = request.POST['description']
        a_price = request.POST['price']
        a_photo = request.FILES.get('photo') 
        print(new_model,a_fuel,a_kilometers,a_description,a_price,a_photo)
        rental_cars = Rentalcar( car_model = new_model, fuel = a_fuel, kilometer = a_kilometers, description = a_description, price = a_price, photo = a_photo )
        rental_cars.save()
        messages.success(request,'Successfully added Rental Cars')
        return redirect('rentalcars')
    
@login_required( login_url= 'login' )
def delete_rental(request,p):
    try:
        rental_car = Rentalcar.objects.get( id = p )
        rental_car.delete()
    except:
        pass
    return redirect('rentalcars')


# Sales Car Views 

@login_required( login_url= 'login' )
def salesCar(request):
    sales_car = Salescar.objects.all()
    details = {'cars':sales_car}
    return render(request,'admin/salescar.html',details)

@login_required( login_url= 'login' )
def addSalesCar(request):
    brand = Carbrand.objects.all()
    context = { 'brand' : brand }
    return render(request,'admin/addsalescar.html',context)

@login_required( login_url= 'login' )
def model_filters(request,i):
    global b
    b=Carbrand.objects.get(id=i)
    models=Carmodel.objects.filter(brands=b)
    dicta = {'models':models}
    return render(request,'admin/addsalescar.html',dicta)

@login_required( login_url= 'login' )
def addSaleCarDetail(request):
    if request.method == 'POST':
        s_model = request.POST['model']
        new_model = Carmodel.objects.get( id = s_model )
        s_fuel = request.POST['fuel']
        s_kilometer = request.POST['kilometers']
        s_description = request.POST['description']
        s_price = request.POST['price']
        s_photo = request.FILES.get('photo')
        print(new_model,s_fuel,s_kilometer,s_kilometer,s_description,s_price,s_photo)
        sale_car = Salescar( car_model = new_model, fuel = s_fuel, kilometer = s_kilometer, description = s_description, price = s_price, photo = s_photo )
        sale_car.save()
        messages.success(request,'Successfully added Sales Car')
        return redirect('salescars')

def deletesalescar(request, sale_id):
    sales_car = Salescar.objects.get( id = sale_id )
    sales_car.delete()
    messages.success(request,'Your second car has been deleted')
    return redirect('salescars')


# Customer Rent Bookings and Pre-Booking Car 

# Sales Car Pre-Booking 

@login_required( login_url= 'login' )
def second_car(request):
    car_sales_data = CarSales.objects.all()
    context = {
        'details': car_sales_data

    }
    return render(request,'admin/booking-details.html',context)


# Rental Car Booking Details 

@login_required(login_url='login')
def rent_car_details(request):
    carbookings = Carbooking.objects.all()
    context = {
        'details': carbookings
    }
    return render(request,'admin/rent-booking-details.html',context)