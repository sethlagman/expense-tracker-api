from django.shortcuts import render
from rest_framework import viewsets
from .models import Expense
from .serializer import ExpenseSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'title', 'category', 'amount']