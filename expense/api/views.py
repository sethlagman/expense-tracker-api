from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Expense
from .serializer import ExpenseSerializer, UserRegistrationSerializer, UserLoginSerializer
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django_filters import FilterSet, ChoiceFilter, DateFilter
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema

class ExpenseFilter(FilterSet):
    CHOICES = [
    ('past_week', 'Past Week'),
    ('past_month', 'Past Month'),
    ('past_three_month', 'Past Three Months')
    ]
    
    date_filter = ChoiceFilter(choices=CHOICES, method='filter_by_date', label='Date Filter')
    start_date = DateFilter(field_name="creation_date", lookup_expr='gte', label='Start Date')
    end_date = DateFilter(field_name="creation_date", lookup_expr='lte', label='End Date')

    class Meta:
        model = Expense
        fields = ['id', 'title', 'category', 'amount']

    def filter_by_date(self, queryset, name, value):
        past_week_date =  str(date.today() - timedelta(days=7))
        past_wmonth_date =  str(date.today() - relativedelta(months=1))
        past_three_month_date =  str(date.today() - relativedelta(months=3))
        
        if value == 'past_week':
            return queryset.filter(creation_date__gte=past_week_date)
        if value == 'past_month':
            return queryset.filter(creation_date__gte=past_wmonth_date)
        if value == 'past_three_month':
            return queryset.filter(creation_date__gte=past_three_month_date)
        
        return queryset


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExpenseFilter
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super(ExpenseViewSet, self).get_queryset()
        user = self.request.user
        queryset = Expense.objects.filter(created_by=user)
        return queryset
    
    @extend_schema(
            description="Get method for expense list",
            summary="Retrieves a list of expenses"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
            description="Post method for creating expense",
            summary="Creates new expense"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
            description="Get method for expense id",
            summary="Retrieve a specific task by its ID"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
            description="Put method for updating expense",
            summary="Update an existing task",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(
            description="Delete method for deleting expense",
            summary="Deletes an existing task"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @extend_schema(
            description="Patch method for partially updating expense",
            summary="Partially updates an existing task"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class UserRegistrationView(GenericAPIView):
    model = User
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    @extend_schema(
            description="Post method for registering user",
            summary="Creates a user"
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            data = serializer.data
            data['response'] = 'Registration successful!'
            token = RefreshToken.for_user(user)
            data['refresh'] = str(token)
            data['access'] = str(token.access_token)
        
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    @extend_schema(
            description="Post method for logging in user",
            summary="Logs in a user"
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token = RefreshToken.for_user(user)

            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'refresh': str(token),
                'access': str(token.access_token)
            })

        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
