from django.core.management.base import BaseCommand
import pandas as pd
import pandas_datareader.data as data
from kabu_django3.settings import BASE_DIR
from stocks.models import Test, Brand, Trades
from datetime import datetime as dt
import datetime


def reg_TSE_from_stooq():
    print("start get from STOOQ")
    all_brands = Brand.objects.all()
    for brand in all_brands:
        code = brand.code
        nation = brand.nation
        brand_code = str(code) + "." + nation
        print("start " + brand_code)
        if Trades.objects.filter(brand_code=brand_code) == 0:
            brand = Brand.objects.get(code=code, nation=nation)
            start = dt(1999, 1, 1)
            end = dt.today() + datetime.timedelta(days=1)
            df = data.DataReader(brand_code, "stooq", start, end)
            df.reset_index(inplace=True)
            df = df.rename(columns={"index": "Date"})
            df_trades = df.to_dict(orient='records')
            trades_insert = []
            for d in df_trades:
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
            print(str(code) + " " + brand.brand_name + " is DONE")
    print("get TSE from Stooq is DONE!")


# BaseCommandを継承して作成
class Command(BaseCommand):
    help = "register TSE brands"

    def handle(self, *args, **options):
        reg_TSE_from_stooq()
