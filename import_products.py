import os
import django
import csv


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BizFlow.settings')
django.setup()

from product.models import Product, Category

with open('product_list.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        category_name = row['دسته‌بندی']
        category, _ = Category.objects.get_or_create(name=category_name)

        Product.objects.update_or_create(
            name=row['نام محصول'],
            category=category,
            description=row['توضیحات'],
            price=float(row['قیمت (تومان)'].replace(',', '')),
            inventory=int(row['موجودی']),
        )
print("Import done ✅")


