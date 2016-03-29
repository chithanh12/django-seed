from django.db import models

# Create your models here.

class Product(models.Model):
    product_code = models.CharField(max_length = 10)
    product_name = models.CharField(max_length = 250)
    description = models.TextField()
    specification = models.TextField()
    stock = models.IntegerField(default =0)
    price = models.IntegerField(default=0)
    sale  = models.IntegerField(default=0)
    thumbnail = models.CharField(max_length = 300)
    created_date = models.DateField( auto_now_add=True)
    def __str__(self):
        return self.product_code

# product Image model
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.CharField(max_length = 300)
        
    