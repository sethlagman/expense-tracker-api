from django.urls import path, include
from rest_framework import routers
from api.views import ExpenseViewSet, UserRegistrationView, UserLoginView

class CustomDefaultRouter(routers.DefaultRouter):

    def get_api_root_view(self, api_urls=None):
        original_root_view = super().get_api_root_view(api_urls)

        def custom_root_view(request, *args, **kwargs):
            response = original_root_view(request)

            additional_links = {
                'register': 'http://127.0.0.1:8000/register/',
                'login': 'http://127.0.0.1:8000/login/',
            }
            response.data.update(additional_links)
            return response
        
        return custom_root_view


router = CustomDefaultRouter()
router.register(r'expense', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login')
]