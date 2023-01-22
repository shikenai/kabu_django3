from django.core.management.base import BaseCommand
import pandas as pd
import pandas_datareader.data as data
from kabu_django3.settings import BASE_DIR
from stocks.models import Test, Brand, Trades
from datetime import datetime as dt
import datetime


def reg_TSE_from_stooq():
    nation = "jp"
    code = 7203
    brand = Brand.objects.get(code=code, nation=nation)

    print("get_STOOQ")
    brand_code = str(code) + "." + nation
    start = dt(1950, 1, 1)
    end = dt.today() + datetime.timedelta(days=1)
    df = data.DataReader(brand_code, "stooq", start, end)
    df.to_csv("data/stooq.csv")
    df = pd.read_csv('data/stooq.csv')
    df_trades = df.to_dict(orient='records')
    trades_insert = []
    for d in df_trades:
        print(d["Date"])
        print(d["Open"])
        print(d["Close"])
        print(d["High"])
        print(d["Low"])
        print(d["Volume"])
        _d = Trades.objects.filter(trade_date=d["Date"], brand_code=brand_code)
        if _d.count() == 0:
            trades_insert.append(Trades(
                brand=brand,
                brand_code=brand_code,
                trade_date=d["Date"],
                open_value=d["Open"],
                close_value=d["Close"],
                high_value=d["High"],
                low_value=d["Low"],
                volume=d["Volume"]
            ))
    Trades.objects.bulk_create(trades_insert)


# BaseCommandを継承して作成
class Command(BaseCommand):
    help = "register TSE brands"

    def handle(self, *args, **options):
        reg_TSE_from_stooq()
