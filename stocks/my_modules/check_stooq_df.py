from django.core.management.base import BaseCommand
import pandas as pd
import pandas_datareader.data as data
from datetime import datetime as dt
import datetime


def check_stooq_df():
    code = 2193
    nation = "jp"
    brand_code = str(code) + "." + nation
    start = dt(1999, 1, 1)
    end = dt.today() + datetime.timedelta(days=1)
    df = data.DataReader(brand_code, "stooq", start, end)
    # print(df)
    print("-----")
    print(df.isna().sum())
    print(df.tail(1))

check_stooq_df()
# # BaseCommandを継承して作成
# class Command(BaseCommand):
#     help = "register TSE brands"
#
#     def handle(self, *args, **options):
#         check_stooq_df()
