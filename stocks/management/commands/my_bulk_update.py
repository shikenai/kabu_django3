from django.core.management.base import BaseCommand
import pandas as pd
import pandas_datareader.data as data
from kabu_django3.settings import BASE_DIR
from stocks.models import Test, Brand
from datetime import datetime as dt


def update():
    print("run update")
    brands = Brand.objects.all()
    for b in brands:
        b.nation = "jp"
    Brand.objects.bulk_update(brands, fields=["nation"])


# BaseCommandを継承して作成
class Command(BaseCommand):
    help = "register TSE brands"

    def handle(self, *args, **options):
        update()