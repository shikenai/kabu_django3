from django.core.management.base import BaseCommand
import pandas_datareader.data as data
from stocks.models import Brand, Trades
from datetime import datetime as dt
import datetime
import time


def reg_TSE_from_stooq():
    print("start get from STOOQ")
    all_brands = Brand.objects.all()
    for brand in all_brands:
        code = brand.code
        nation = brand.nation
        brand_code = str(code) + "." + nation
        print("start " + brand_code)
        if Trades.objects.filter(brand_code=brand_code).exists():
            pass
        else:
            t1 = time.time()
            start = dt(1999, 1, 1)
            end = dt.today() + datetime.timedelta(days=1)
            df = data.DataReader(brand_code, "stooq", start, end)
            if "Volume" in df.columns:
                df["Volume"] = df["Volume"].fillna(0).astype("int")
            df.reset_index(inplace=True)
            df = df.rename(columns={"index": "Date"})
            df_trades = df.to_dict(orient='records')
            brand = Brand.objects.get(code=code, nation=nation)
            trades_insert = []
            for d in df_trades:
                # if Trades.objects.filter(trade_date=d["Date"], brand_code=brand_code).exists():
                #     pass
                # else:
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
            print(time.time() - t1)
    print("get TSE from Stooq is DONE!")


def returning(x, y):
    return x + y


def test(wei):
    print("test command")
    print(wei)
    print(returning(1, 9))


# BaseCommandを継承して作成
class Command(BaseCommand):
    help = "register TSE brands"

    def add_arguments(self, parser):
        parser.add_argument("first", type=str)

    def handle(self, *args, **options):
        if options["first"] == "reg":
            reg_TSE_from_stooq()
        elif options["first"] == "test":
            test()
