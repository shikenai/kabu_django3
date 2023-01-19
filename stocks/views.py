from django.shortcuts import render
from stocks.my_modules import my_function, sub_function


# Create your views here.
def index(request):
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