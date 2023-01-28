from django.core.management.base import BaseCommand
import pandas_datareader.data as data
from stocks.models import Brand, Trades
from datetime import datetime as dt
import datetime
import time


def test():
    print('test2023')

# BaseCommandを継承して作成
class Command(BaseCommand):
    help = "register TSE brands"

    def add_arguments(self, parser):
        parser.add_argument("first", type=str)

    def handle(self, *args, **options):
        test()
