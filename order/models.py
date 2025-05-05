from django.db import models
from account.models import Department

class Order(models.Model):
    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    total_cost = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=50, blank=True, null=True)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
