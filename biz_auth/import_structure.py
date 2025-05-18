import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BizAuth.settings')
django.setup()

from account.models import Department, Role

with open('company_structure.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row.keys())
        department_name = row['بخش']
        department, _ = Department.objects.get_or_create(department=department_name)

        Role.objects.update_or_create(
            department=department,
            role=row['عنوان شغلی'],
            responsibility=row['شرح وظایف'],
        )
print("Import done ✅")
