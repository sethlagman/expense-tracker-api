from django.urls import path, include
from rest_framework import routers
from api.views import ExpenseViewSet, UserRegistrationView, UserLoginView

router = routers.DefaultRouter()
router.register(r'expense', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login')
]