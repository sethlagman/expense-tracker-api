from django.urls import path, include
from rest_framework import routers, permissions
from api.views import ExpenseViewSet, UserRegistrationView, UserLoginView
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

class CustomDefaultRouter(routers.DefaultRouter):

    def get_api_root_view(self, api_urls=None):
        original_root_view = super().get_api_root_view(api_urls)

        def custom_root_view(request, *args, **kwargs):
            response = original_root_view(request)

            additional_links = {
                'register': 'http://127.0.0.1:8000/register/',
                'login': 'http://127.0.0.1:8000/login/',
                'docs': 'http://127.0.0.1:8000/docs/',
                'schema': 'http://127.0.0.1:8000/schema/',
                'refresh': 'http://127.0.0.1:8000/refresh/',
            }
            response.data.update(additional_links)
            return response
        
        return custom_root_view


router = CustomDefaultRouter()
router.register(r'expense', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]