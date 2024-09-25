import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from app.models import Customer, Order  # Replace 'myapp' with your actual app name

class Command(BaseCommand):
    help = 'Generate 100 sample records for Customer and Order models'

    def handle(self, *args, **kwargs):
        # Generate 20 customers
        customers = []
        for i in range(20):
            customer = Customer.objects.create(
                name=f'Customer {i+1}',
                email=f'customer{i+1}@example.com'
            )
            customers.append(customer)

        # Generate 100 orders
        for _ in range(100):
            order = Order.objects.create(
                customer=random.choice(customers),
                status=random.choice(['Pending', 'Completed', 'Cancelled']),
                amount=round(random.uniform(20.00, 500.00), 2),  # Random amount between 20.00 and 500.00
                date=datetime.now() - timedelta(days=random.randint(0, 365))  # Random date within the past year
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 100 sample records'))
