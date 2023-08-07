from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('edit',views.edit,name='edit'),
    path('editdetail',views.editDetails,name='editdetail'),
    path('change-password',views.changePassword,name='changepassword'),
    path('newpassword',views.newpassword,name='newpassword'),
    # Rental Cars
    path('car-rent',views.rentalcars,name='carrental'),
    path('bookings/<int:i>',views.book,name='bookings'),
    path('rentbook/<int:rent_car>',views.create_booking,name='rentbook'),
    path('rental-car/booking',views.myBooking,name='bookings'),
    path('deletebooking/<int:car_id>',views.deletebooking,name='deletebooking'),
    # Second Hand Cars
    path('salescar',views.salespage,name='salescar'),
    path('sales-booking/<int:i>',views.sales_Booking,name='salesbookings'),
    path('addsalesbooking/<int:sales_car_id>',views.create_sales_booking,name='addsalesbooking'),
    path('sales',views.salesbookingcar,name='sales'),
    path('deletesale/<int:sale_id>',views.deletesalesbooking,name = 'deletesale'),
    path('filtercar<int:car_brand_id',views.model_filter_car,name = 'filtercar'),
    # Payment
    path('payment_success',views.payment_success,name='paymentsuccess'),
    path('payment_failed',views.payment_failed,name='paymentfailed'),
    path('booking/<int:booking_id>/payment',views.confirm_payment,name='razorpaypayment'),
]