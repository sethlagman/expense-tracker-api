from django.shortcuts import render
from rest_framework import viewsets
from .models import Expense
from .serializer import ExpenseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django_filters import FilterSet, BooleanFilter

class ExpenseFilter(FilterSet):
    pastweek = BooleanFilter(method='filter_by_past_week', label='Past Week')
    pastmonth = BooleanFilter(method='filter_by_past_month', label='Past Month')
    past_three_month = BooleanFilter(method='filter_by_past_three_month', label='Past Three Months')

    class Meta:
        model = Expense
        fields = ['id', 'title', 'category', 'amount']

    def filter_by_past_week(self, queryset, name, value):
        pastweek_date =  str(date.today() - timedelta(days=7))

        if value:
            return queryset.filter(creation_date__gte=pastweek_date)
        return queryset
    
    def filter_by_past_month(self, queryset, name, value):
        pastwmonth_date =  str(date.today() - relativedelta(months=1))

        if value:
            return queryset.filter(creation_date__gte=pastwmonth_date)
        return queryset

    def filter_by_past_three_month(self, queryset, name, value):
        past_three_month_date =  str(date.today() - relativedelta(months=3))

        if value:
            return queryset.filter(creation_date__gte=past_three_month_date)
        return queryset

    
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExpenseFilter