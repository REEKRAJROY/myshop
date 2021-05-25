from django.http import HttpResponse
from django.shortcuts import render  #might have to remove later
from.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',
                    {'products':products})

def new(request):
    return HttpResponse('New Products')