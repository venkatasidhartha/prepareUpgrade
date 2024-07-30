from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False,blank=False)

    def __str__(self):
        return self.name    
    
class Orders(models.Model):
    product = models.CharField(max_length=200, null=False, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False,blank=False)

    def __str__(self):
        return self.product