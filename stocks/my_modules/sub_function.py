from kabu_django3.settings import BASE_DIR
import os

import requests
import pandas as pd


# from stocks import models


# # ----------------------------------------------------
# # 東証から銘柄一覧を取得して、dataフォルダに格納する一連の関数
def save_file(path, filename, data, mode):
    # ファイルを保存するためのディレクトリを作成
    os.makedirs(path, exist_ok=True)

    # ファイルパスを生成
    file_path = os.path.join(path, filename)
    print(file_path)

    # 指定したフォルダに保存
    with open(file_path, mode) as f:
        f.write(data.content)


def brand_xls2csv():
    read_file = pd.read_excel(BASE_DIR / "data/data_all_brand.xls")
    read_file.to_csv(BASE_DIR / "data/data_all_brand.csv", index=True, header=True, encoding="utf-8")


def get_all_brand():
    # 東証一部上場企業の一覧を取得
    req = requests.get("https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls")

    # 保存先ディレクトリのパス
    print(BASE_DIR)
    print(type(BASE_DIR))
    # new_dir = os.path.join(BASE_DIR, "data")
    new_dir = BASE_DIR / 'data'

    # 保存するファイル名
    filename = "data_all_brand.xls"

    # ファイルを保存する
    save_file(new_dir, filename, req, "wb")

    brand_xls2csv()

get_all_brand()

# # --------------------------------------------------
#
# def register_TSE_brand():
#     df = pd.read_csv("/Users/yoshikazukakehashi/PycharmProjects/kabu_django2/data/data_all_brand.csv", encoding="utf-8")
#
#     print(df.columns)
#     ## 各リストを作成
#     # 市場名
#     list_market = []  # 市場名（ここでは「東証１部」が望ましい）
#     for i in range(df.shape[0]):
#         list_market.append('東証')
#     # 銘柄名
#     list_brand_name_zenkaku = df['銘柄名'].to_list()  # 銘柄名
#     list_brand_name = [s.replace('\u3000', ' ') for s in list_brand_name_zenkaku]
#     # コード
#     list_code = df['コード'].to_list()  # コード 型判定したらしっかりとintでした○）
#     print(type(list_code[0]))
#     list_division = df['市場・商品区分'].to_list()  # 市場・商品区分
#     list_industry_code_1 = df['33業種コード'].to_list()  # 33業種コード
#     list_industry_division_1 = df['33業種区分'].to_list()  # 33業種区分
#     list_industry_code_2 = df['17業種コード'].to_list()  # 17業種コード
#     list_industry_division_2 = df['17業種区分'].to_list()  # 17業種区分
#     list_scale_code = df['規模コード'].to_list()  # 規模コード
#     list_scale_division = df['規模区分'].to_list()  # 規模区分
#
#
# def register_TSE_brand2():
#     n = 5
#     list_market = []  # 市場名（ここでは「東証１部」が望ましい）
#     for i in range(n):
#         list_market.append('東証')
#
#     list_code = [1, 2, 3, 4, 5]
#     list_brand_name = ["sasaki", "kawano", "watanabe", "mori", "usuki"]
#
#     brand_objects = []
#     for j in range(n):
#         brand_objects.append(models.Brand(market=list_market[j], brand_name=list_brand_name[j], code=list_code[j]))
#
#     print(brand_objects)
#
#
# register_TSE_brand()
