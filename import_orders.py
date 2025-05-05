import os
import django
import csv


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BizFlow.settings')
django.setup()
from account.models import Department
from product.models import Product, Category
from order.models import Order

with open('orders.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        department_name = row['نقش']
        department, _ = Department.objects.get_or_create(department=department_name)

        Order.objects.update_or_create(
            title=row['عنوان درخواست'],
            department=department,
            description=row['شرح'],
            total_cost=float(row['هزینه تقریبی (تومان)'].replace(',', '')),
            status=row['وضعیت'],
        )
print("Import done ✅")


