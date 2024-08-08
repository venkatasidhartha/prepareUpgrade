from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    price = models.CharField(max_length=255,blank=False,null=False)
    created_at = models.DateTimeField(auto_now=True)
