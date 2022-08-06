from django.contrib import admin
import json
from .models import Trendyol
import sqlite3


class TrendyolAdmin(admin.ModelAdmin):
#     connection = sqlite3.connect('db.sqlite')
#     cursor = connection.cursor()

#     traffic = json.load(open('samples.json'))
#     columns = ['product_name','brand','product_price','product_discount_price','product_is_promoted',
#       'sub_category_name','sales_ch','city','score','sellers_name','city_names','seller_scores']
#     for row in traffic:
#         keys= tuple(row[c] for c in columns)
#         cursor.execute(f'insert into learn_products values(?,?,?,?,?,?,?,?,?,?,?)',keys)
    list_display=('product_name','brand','product_price','product_discount_price','product_is_promoted',
'sub_category_name','sales_ch','city','score','sellers_name','city_names','seller_scores')

admin.site.register(Trendyol, TrendyolAdmin)

# Register your models here.
