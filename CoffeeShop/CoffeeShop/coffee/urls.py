from django.urls import path
from coffee import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('payment/', views.payment_page, name='payment_page'),
    path('payment/success/', views.payment_success, name='payment_success'), 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),  
]