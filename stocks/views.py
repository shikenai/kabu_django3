from django.shortcuts import render
from stocks.my_modules import sub_function
from stocks.management.commands import my_function, my_bulk_update, reg_prices
from stocks.models import Brand, Trades
import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf


# Create your views here.
def index(request):
    _brands = Brand.objects.all()
    contents = {
        "brand": _brands
    }
    return render(request, 'index.html', contents)


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
        pass
        # my_function.get_stooq()
        # my_bulk_update.update()
    else:
        print('else')
    return render(request, 'index.html')


def reg_TSE_from_stooq(request):
    if request.method == 'POST':
        print("reg_from stooq")
        reg_prices.reg_TSE_from_stooq()
    else:
        print('else')
    return render(request, 'index.html')


def company(request):
    code = 7203
    nation = "jp"
    brand_code = str(code) + "." + nation
    _brand = Brand.objects.get(code=code, nation=nation)
    _trades = Trades.objects.filter(brand=_brand).order_by("trade_date")
    df = pd.DataFrame(list(_trades.values()))
    print(df.columns)
    df.set_index("Date")
    mpf.plot(df)
    return render(request, 'company.html')