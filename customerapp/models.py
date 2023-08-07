from django.db import models
from django.contrib.auth.models import User
from adminapp.models import Rentalcar,Salescar
# Create your models here.


class Customer(models.Model):
    c_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10,blank=True,null=True,default='')
    city = models.CharField(max_length=100,default="")
    state = models.CharField(max_length=100,default='')
    photo = models.ImageField(upload_to='images/customer',blank=True)


# Rent car
class Rentbooking(models.Model):
    rental_car = models.ForeignKey(Rentalcar,on_delete=models.CASCADE,null=True)
    pick_up = models.DateField( auto_now=True)
    drop_off = models.DateField()
    total_price = models.FloatField(null=True)

class Carbooking(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    rent_car = models.ManyToManyField(Rentbooking)
    payment_id = models.CharField(max_length=100,null=True)
    payment_status = models.BooleanField(default=False)
    


# sales car
class CarSalesCus(models.Model):
    car = models.ForeignKey(Salescar,on_delete = models.CASCADE,null=True)
    booking_date = models.DateField(auto_now= True)
    confirm_date = models.DateField(null=True)
    total_price = models.FloatField()

class CarSales(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    sales_Car = models.ManyToManyField(CarSalesCus) 