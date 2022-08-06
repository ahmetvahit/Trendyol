from django.db import models

class Trendyol(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_discount_price = models.FloatField()
    product_is_promoted = models.CharField(max_length=50)
    sub_category_name = models.CharField(max_length=50,null=True)
    sales_ch = models.CharField(max_length=70,null=True)
    city = models.TextField(max_length=50,null=True)
    score = models.FloatField(null=True)
    sellers_name = models.CharField(max_length=500,null=True)
    city_names = models.CharField(max_length=500,null=True)
    seller_scores = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.product_name
# Create your models here.
