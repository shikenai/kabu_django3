from django.shortcuts import render
from stocks.my_modules import sub_function
from stocks.management.commands import my_function
from stocks.models import Test


# Create your views here.
def index(request):
    my_function.bulk_create_test()
    my_function.register_TSE_brand()
    return render(request, 'index.html')


def get_all_brand_in_TSE():
    sub_function.get_all_brand()


def reg_test(request):
    if request.method == 'POST':
        print("post")
        sub_function.get_all_brand()
    else:
        print('else')
    return render(request, 'index.html')
