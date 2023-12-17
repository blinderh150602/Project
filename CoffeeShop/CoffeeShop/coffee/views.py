from django.shortcuts import render
from django.http import HttpResponse
from coffee.models import coffee 
from django.shortcuts import render, redirect
# Create your views here.
def home (request):
    coffee2 = coffee.objects.all()
    return render(request, 'home.html',{'coffee':coffee2})
def payment_page(request):
    if request.method == 'POST':
        return redirect('payment_success')
    return render(request, 'payment/payment_page.html')
def payment_success(request):
    return render(request, 'payment/success.html')
def login(request):
    return render(request, 'customer/login.html')
def logout(request):
    return render(request, 'customer/logout.html')

