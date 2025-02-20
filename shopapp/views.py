from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')


def images(request):
    return render(request,'gallery.html')

def about(request):
    return render(request,'about.html')

def registarion(request):
    return render(request,'Registration.html')

def products(request):
    return render(request,'products.html')
