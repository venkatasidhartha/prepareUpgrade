from django.db import models

# Create your models here.

class Orders(models.Model):
    status_choice = (
        ("Oreder Pending","Oreder Pending"),
        ("Oreder Confirmed","Oreder Confirmed"),
        ("Payment Cancelled","Payment Cancelled"),
        ("Payment Failed","Payment Failed"),
    )
    product_id = models.IntegerField(blank=False,null=False)
    quanity = models.PositiveIntegerField(blank=False,null=False)
    price = models.FloatField(blank=False,null=False)
    user_id = models.IntegerField(blank=False,null=False)
    status = models.CharField(max_length=255,choices=status_choice,blank=False,null=False,default="Oreder Pending")
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

