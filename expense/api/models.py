from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORIES = [
        ('Groceries', 'Groceries'),
        ('Leisure', 'Leisure'),
        ('Electronics', 'Electronics'),
        ('Utilities', 'Utilities'),
        ('Clothing', 'Clothing'),
        ('Health', 'Health'),
        ('Others', 'Others')
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=25, choices=CATEGORIES)
    description = models.CharField(max_length=100)
    amount = models.PositiveBigIntegerField()
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
