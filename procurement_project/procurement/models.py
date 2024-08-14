from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Procurement(models.Model):
    BRANCH_CHOICES = [
        ('Branch A', 'Branch A'),
        ('Branch B', 'Branch B'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    ]

    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    bill = models.FileField(upload_to='bills/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return f"{self.item} - {self.branch} - {self.status}"