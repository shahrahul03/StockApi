from django.db import models


class StockDB(models.Model):
    company_name = models.CharField(max_length=255)
    opening_price = models.FloatField()
    closing_price = models.FloatField()
    date = models.DateField(auto_now_add=True)
