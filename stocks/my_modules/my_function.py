import pandas as pd
from kabu_django3.settings import BASE_DIR
from stocks.models import Test
df = pd.read_csv(BASE_DIR / "data/test.csv")

df_records = df.to_dict(orient='records')
# print(df_records)

test_model_inserts = []
for d in df_records:
    print(d)
    print(d["コード"])
    print(d["銘柄名"])
#     test_model_inserts.append(Test(
#         num=d[0],
#         name=d[1]
#     ))
# Test.objects.bulk_create(test_model_inserts)