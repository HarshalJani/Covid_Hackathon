from django.shortcuts import render
from django.http import QueryDict

# Create your views here.
def index(request):
    return render(request,'covid_inventary/index.html')

def dashboard(request):
    return render(request,'covid_inventary/dashboard.html')

def login(request):
    return render(request,'covid_inventary/login.html')

def inventory(request):
    if request.method == 'POST':
        if request.POST.__contains__('isVendor'):
            return render(request,'covid_inventary/storage.html')
        else:
            return render(request,'covid_inventary/inventory.html')