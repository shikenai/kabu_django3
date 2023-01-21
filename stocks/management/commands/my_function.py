from django.core.management.base import BaseCommand
import pandas as pd
import pandas_datareader.data as data
from kabu_django3.settings import BASE_DIR
from stocks.models import Test, Brand
from datetime import datetime as dt


def update():
    brands = Brand.objects.all()
    for b in brands:
        b.nation = "jp"
    Brand.objects.bulk_update(brands, fields="nation")


# ---------------------
def register_TSE_brand():
    df = pd.read_csv(BASE_DIR / "data/data_all_brand.csv")

    df_records = df.to_dict(orient='records')

    brand_model_inserts = []
    for d in df_records:
        _brands = Brand.objects.filter(code=d["コード"])
        if _brands.count() == 0:
            brand_model_inserts.append(Brand(
                nation="日本",
                market="東証１部",
                brand_name=d["銘柄名"],
                code=d["コード"],
                division=d["市場・商品区分"],
                industry_code_1=d['33業種コード'],
                industry_division_1=d['33業種区分'],
                industry_code_2=d['17業種コード'],
                industry_division_2=d['17業種区分'],
                scale_code=d['規模コード'],
                scale_division=d['規模区分']
            ))
    Brand.objects.bulk_create(brand_model_inserts)


# ---------------------

# def get_stooq():
#     print("get_STOOQ")
#     brand = "7203.JP"
#     start = dt(1950, 1, 1)
#     end = dt.today() + datetime.timedelta(days=1)
#     df = data.DataReader(brand, "stooq", start, end)
#     df_prices = df.to_dict(orient='records')
#     prices_insert = []
#     # Index(['Open', 'High', 'Low', 'Close', 'Volume'], dtype='object')
#     for d in df_prices:
#
#     print(df.columns)


# BaseCommandを継承して作成
class Command(BaseCommand):
    help = "register TSE brands"

    def handle(self, *args, **options):
        register_TSE_brand()
