import pandas_datareader.data as data
from datetime import datetime as dt
import datetime


def check_stooq_df():
    # code = 1485
    code = 2193
    nation = "jp"
    brand_code = str(code) + "." + nation
    start = dt(1999, 1, 1)
    end = dt.today() + datetime.timedelta(days=1)
    df = data.DataReader(brand_code, "stooq", start, end)
    # print(df)
    print("-----")
    print(df.columns)
    if "Volume" in df.columns:
        df["Volume"] = df["Volume"].fillna(0).astype("int")
        print(df)
    else:
        print("NONE")
    # print(print(df["Volume"]))


check_stooq_df()
# # BaseCommandを継承して作成
# class Command(BaseCommand):
#     help = "register TSE brands"
#
#     def handle(self, *args, **options):
#         check_stooq_df()
