from django.db import models

# Create your models here.


class Product(models.Model):
    BOOLEAN_CHOICES = (
        (0, 'No'),
        (1, 'Yes'),
    )
    name = models.CharField(max_length=255,blank=False,null=False)
    price = models.CharField(max_length=255,blank=False,null=False)
    show_web = models.IntegerField(choices=BOOLEAN_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now=True)
