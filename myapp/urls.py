from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .form import MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginPage,name='login'),
    path('register',views.signUpPage,name='register'),
    path('reset-password',views.resetPassword,name='resetpassword'),
    path('signup',views.signUp,name='signup'),
    path('signin',views.signIn,name='signin'),
    path('logout',views.signOut,name='logout'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name = 'auth/forgot-password-email.html',form_class = MyPasswordResetForm),name='passwordReset'),
    path('reset_password/Done',auth_views.PasswordResetDoneView.as_view(template_name = 'auth/password-send-email.html'), name='password_reset_done'),
    path('reset-password-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'auth/reset-password.html',form_class = MySetPasswordForm),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view( template_name = 'auth/password-confirm.html'),name='password_reset_complete')
]   