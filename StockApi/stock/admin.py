from django.contrib import admin
from .models import StockDB
# Register your models here.
@admin.register(StockDB)
class StockAdmin(admin.ModelAdmin):
    list_display=['id','company_name','opening_price','closing_price','date']
    