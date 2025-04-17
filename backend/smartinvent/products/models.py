from django.db import models
from django.contrib.postgres.indexes import GinIndex
from .managers import ProductManager




class Product(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
    objects = models.Manager()
    special = ProductManager()
    
    class Meta:
        indexes = [
            GinIndex(fields=['name'], name='name_gin_indx')
        ]
       



class ProductReplenishment(models.Model):
    active = models.BooleanField(default=False)
    defaultValue = models.IntegerField()
    providerEmail = models.EmailField()
    providerName = models.CharField(max_length=40)
    address = models.CharField(max_length=70,blank=True,null=True)
    providerNumber = models.IntegerField(blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True,related_name='provider')


