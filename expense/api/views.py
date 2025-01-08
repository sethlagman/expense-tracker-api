from django.shortcuts import render
from rest_framework import viewsets
from .models import Expense
from .serializer import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
