from django.db import models


# Create your models here.


class Carbrand(models.Model):
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.brand

class Carmodel(models.Model):
    brands = models.ForeignKey(Carbrand,on_delete=models.CASCADE,null=True)
    models = models.CharField(max_length=100)

class Rentalcar(models.Model):
    car_model = models.ForeignKey(Carmodel,on_delete=models.CASCADE,null=True)
    fuel = models.CharField(max_length=100,default='',blank=True,null=True)
    kilometer = models.IntegerField()
    description = models.CharField(max_length=300)
    price = models.FloatField()
    photo = models.ImageField(upload_to='images/cars',blank=True)
    
class Salescar(models.Model):
    car_model = models.ForeignKey(Carmodel,on_delete=models.CASCADE,null=True)
    fuel = models.CharField(max_length=50,default='',null=True)
    kilometer = models.IntegerField()
    description = models.CharField(max_length=300)
    price = models.FloatField()
    photo = models.ImageField(upload_to='sales/cars',blank=True)