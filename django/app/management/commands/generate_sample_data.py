import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from app.models import Product, Sale  # Replace 'myapp' with the actual app name

class Command(BaseCommand):
    help = 'Generate 100 sample records for Product and Sale models'

    def handle(self, *args, **kwargs):
        # Generate 10 products
        products = []
        for i in range(10):
            product = Product.objects.create(
                name=f'Product {i+1}',
                price=round(random.uniform(10.00, 100.00), 2)  # Random price between 10.00 and 100.00
            )
            products.append(product)

        # Generate 100 sales
        for _ in range(100):
            sale = Sale.objects.create(
                product=random.choice(products),
                amount=round(random.uniform(1.00, 20.00), 2),  # Random amount between 1.00 and 20.00
                date=datetime.now() - timedelta(days=random.randint(0, 365))  # Random date within the past year
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 100 sample records'))
