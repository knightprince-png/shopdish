from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')


def images(request):
    return render(request,'gallery.html')

def about(request):
    return render(request,'about.html')
