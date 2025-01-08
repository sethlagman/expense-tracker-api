from django.urls import path, include
from rest_framework import routers
from api.views import ExpenseViewSet

router = routers.DefaultRouter()
router.register(r'expense', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]