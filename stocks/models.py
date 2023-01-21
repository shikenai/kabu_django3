from django.db import models
import datetime as dt

# Create your models here.
from django.db import models


class Brand(models.Model):
    nation = models.CharField(max_length=30, blank=True, null=True, verbose_name='国')
    market = models.CharField(max_length=20, blank=True, null=True)
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    division = models.CharField(max_length=20, blank=True, null=True)
    industry_code_1 = models.CharField(max_length=10, blank=True, null=True)
    industry_division_1 = models.CharField(max_length=10, blank=True, null=True)
    industry_code_2 = models.CharField(max_length=10, blank=True, null=True)
    industry_division_2 = models.CharField(max_length=10, blank=True, null=True)
    scale_code = models.CharField(max_length=10, blank=True, null=True)
    scale_division = models.CharField(max_length=10, blank=True, null=True)

    def unique_code(self):
        return "【" + self.nation + "：" + self.market + "】" + self.brand_name + "(" + str(self.code) + "）"

    def __str__(self):
        return self.brand_name + "(" + self.market + ":" + str(self.code) + ")"


class Prices(models.Model):
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    trade_date = models.DateField(blank=True, null=True, auto_now=True)
    start_value = models.FloatField(verbose_name='始値', blank=True, null=True)
    end_value = models.FloatField(verbose_name='終値', blank=True, null=True)
    max_value = models.FloatField(verbose_name='高値', blank=True, null=True)
    min_value = models.FloatField(verbose_name='安値', blank=True, null=True)

    def __str__(self):
        return "株価" + self.brand.unique_code() + self.trade_date.strftime("%Y年%m月%d日")


class Test(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.num) + self.name
