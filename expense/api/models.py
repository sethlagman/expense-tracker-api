from django.db import models

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

    payment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=25, choices=CATEGORIES)
    description = models.CharField(max_length=100)
    amount = models.PositiveBigIntegerField()
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
