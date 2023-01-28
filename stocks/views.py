from django.shortcuts import render
from stocks.my_modules import sub_function
from stocks.management.commands import my_function, my_bulk_update, reg_prices, descripter
from stocks.models import Brand, Trades
import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf
from django_pandas.io import read_frame
from django.http import HttpResponse


# Create your views here.
def index(request):
    _brands = Brand.objects.all()
    _trades = Trades.objects.filter(brand_code="1485.jp")
    contents = {
        "brand": _brands,
        "trade": _trades
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


def boot_descripter(request):
    df = descripter.get_svg()
    return render(request, "descripter.html", {
        "df": df
    })


def reg_TSE_from_stooq(request):
    if request.method == 'POST':
        print("reg_from stooq")
        # reg_prices.reg_daily_trades(1301, "jp")
        # reg_prices.reg_TSE_from_stooq()
        reg_prices.get_from_list()
        # print("yei")
    else:
        print('else')
    return render(request, 'index.html')


def company(request):
    code = 7203
    nation = "jp"
    _brand = Brand.objects.get(code=code, nation=nation)
    _trades = Trades.objects.filter(brand=_brand).order_by("trade_date")
    df = read_frame(_trades)
    df["trade_date"] = pd.to_datetime(df["trade_date"])
    df = df.set_index("trade_date")
    df = df.reindex(columns=['open_value', 'high_value', 'low_value', 'close_value', 'volume'])
    df = df.rename(columns={'open_value': "Open", 'high_value': "High", 'low_value': "Low", 'close_value': "Close",
                            'volume': "Volume"})
    mpf.plot(df, type="candle")
    return render(request, 'company.html')
