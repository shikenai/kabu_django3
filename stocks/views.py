from django.shortcuts import render
from stocks.my_modules import sub_function
from stocks.management.commands import my_function
from stocks.models import Test


# Create your views here.
def index(request):
    return render(request, 'index.html')


def get_all_brand_in_TSE():
    sub_function.get_all_brand()


def get_TSE(request):
    if request.method == 'POST':
        print("get_TSE")
        sub_function.get_all_brand()
    else:
        print('else')
    return render(request, 'index.html')


def reg_TSE(request):
    if request.method == 'POST':
        print("reg_TSE")
        my_function.register_TSE_brand()
    else:
        print('else')
    return render(request, 'index.html')


def get_stooq(request):
    if request.method == 'POST':
        my_function.get_stooq()
    else:
        print('else')
    return render(request, 'index.html')
