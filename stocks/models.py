from django.db import models

# Create your models here.
from django.db import models


class Brand(models.Model):
    nation = models.CharField(max_length=30, blank=True, null=True, verbose_name='国')
    market = models.CharField(max_length=20, blank=True, null=True)
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    division = models.CharField(max_length=20, blank=True, null=True)
    industry_code_1 = models.IntegerField(blank=True, null=True)
    industry_division_1 = models.CharField(max_length=10, blank=True, null=True)
    industry_code_2 = models.IntegerField(blank=True, null=True)
    industry_division_2 = models.CharField(max_length=10, blank=True, null=True)
    scale_code = models.IntegerField(blank=True, null=True)
    scale_division = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.brand_name + "(" + self.market + ":" + str(self.code) + ")"
