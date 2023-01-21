from django.core.management.base import BaseCommand
import pandas as pd
import pandas_datareader.data as data
from kabu_django3.settings import BASE_DIR
from stocks.models import Test, Brand, Trades
from datetime import datetime as dt
import datetime


def reg_TSE_from_stooq():
    print("get_STOOQ")
    code = 7203
    nation = "jp"
    brand_code = str(code) + "." + nation
    start = dt(1950, 1, 1)
    end = dt.today() + datetime.timedelta(days=1)
    df = data.DataReader(brand_code, "stooq", start, end)
    # print(df["Date"])
    df.to_csv("data/stooq.csv")
    df = pd.read_csv('data/stooq.csv')
    df_trades = df.to_dict(orient='records')
    trades_insert = []
    # 'Date', 'Open', 'High', 'Low', 'Close', 'Volume
    for d in df_trades:
        _d = Trades.objects.filter(brand__code=code, brand__nation=nation, trade_date=d["Date"])
        if _d.count() == 0:
            trades_insert.append(Trades(
                brand=brand_code,
                trade_date=d["Date"],
                start_value=d["Open"],
                end_value=d["Close"],
                max_value=d["High"],
                min_value=d["Low"],
                volume=d["Volume"]
            ))
    Trades.objects.bulk_create(trades_insert)

# BaseCommandを継承して作成
class Command(BaseCommand):
    help = "register TSE brands"

    def handle(self, *args, **options):
        reg_TSE_from_stooq()
