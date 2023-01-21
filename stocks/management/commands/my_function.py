from django.core.management.base import BaseCommand
import pandas as pd
from kabu_django3.settings import BASE_DIR
from stocks.models import Test


def bulk_create_test():
    df = pd.read_csv(BASE_DIR / "data/test.csv")

    df_records = df.to_dict(orient='records')
    # print(df_records)

    test_model_inserts = []
    for d in df_records:
        print("-----")
        print(d)
        print(d["コード"])
        print(d["銘柄名"])
        _tests = Test.objects.filter(num=d["コード"])
        if _tests.count() == 0:
            test_model_inserts.append(Test(
                num=d["コード"],
                name=d["銘柄名"]
            ))
    Test.objects.bulk_create(test_model_inserts)


# BaseCommandを継承して作成
class Command(BaseCommand):
    help = "test bulk insert"

    # def add_arguments(self, parser):
    #     parser.add_argument('blog_id', nargs='+', type=int)

    def handle(self, *args, **options):
        bulk_create_test()
