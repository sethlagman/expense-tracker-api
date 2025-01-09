from django.shortcuts import render
from rest_framework import viewsets
from .models import Expense
from .serializer import ExpenseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django_filters import FilterSet, ChoiceFilter

class ExpenseFilter(FilterSet):
    CHOICES = [
    ('option1', 'Past Week'),
    ('option2', 'Past Month'),
    ('option3', 'Past Three Months')
    ]
    date_filter = ChoiceFilter(choices=CHOICES, method='filter_by_date', label='Date Filter')

    class Meta:
        model = Expense
        fields = ['id', 'title', 'category', 'amount']

    def filter_by_date(self, queryset, name, value):
        pastweek_date =  str(date.today() - timedelta(days=7))
        pastwmonth_date =  str(date.today() - relativedelta(months=1))
        past_three_month_date =  str(date.today() - relativedelta(months=3))
        
        if value == 'option1':
            return queryset.filter(creation_date__gte=pastweek_date)
        if value == 'option2':
            return queryset.filter(creation_date__gte=pastwmonth_date)
        if value == 'option3':
            return queryset.filter(creation_date__gte=past_three_month_date)
        
        return queryset


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExpenseFilter
