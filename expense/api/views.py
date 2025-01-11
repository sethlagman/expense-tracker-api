from django.shortcuts import render
from rest_framework import viewsets
from .models import Expense
from .serializer import ExpenseSerializer, UserRegistrationSerializer, UserLoginSerializer
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django_filters import FilterSet, ChoiceFilter, DateFilter
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

class ExpenseFilter(FilterSet):
    CHOICES = [
    ('option1', 'Past Week'),
    ('option2', 'Past Month'),
    ('option3', 'Past Three Months')
    ]
    
    date_filter = ChoiceFilter(choices=CHOICES, method='filter_by_date', label='Date Filter')
    start_date = DateFilter(field_name="creation_date", lookup_expr='gte', label='Start Date')
    end_date = DateFilter(field_name="creation_date", lookup_expr='lte', label='End Date')

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


class UserRegistrationView(CreateAPIView):
    model = User
    serializer_class = UserRegistrationSerializer


class UserLoginView(CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']

            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email, 
            })
            
        return Response({
            'error': 'User not found',
        })