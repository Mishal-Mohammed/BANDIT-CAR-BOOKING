from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='adminhome'),
    path('users-detail',views.userDetail,name='userdetail'),
    path('rentalcars',views.rentalCars,name='rentalcars'),
    path('addrentalcar', views.addRentalCars, name='addrentalcar'),
    path('carbrand',views.carBrand,name='carbrand'),
    path('addbrand',views.addBrand,name='addbrand'),
    path('addmodel',views.addModel,name='addmodel'),
    path('deletemodel/<int:model_id>',views.deletemodels,name='deletemodel'),
    path('modelfilter/<int:i>',views.model_filter,name='modelfilter'),
    path('salescars',views.salesCar,name='salescars'),
    path('addsalescar',views.addSalesCar,name='addsalescar'),
    path('addrent',views.addrentalcar,name='addrent'),
    path('addsale',views.addSaleCarDetail,name='addsale'),
    path('modelfilters/<int:i>',views.model_filters,name='modelfilters'),
    path('delete/<int:p>',views.delete_rental,name='delete'),
    path('deletesale/<int:sale_id>',views.deletesalescar,name='deletesales'),
    path('second-car-booking',views.second_car,name='secondcarbooking'),
    path('rent-car-booking',views.rent_car_details,name='rentcarsbooking')

]