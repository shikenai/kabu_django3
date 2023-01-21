from django.contrib import admin
from stocks import models
# Register your models here.
admin.site.register(models.Brand)
admin.site.register(models.Test)
admin.site.register(models.Trades)
