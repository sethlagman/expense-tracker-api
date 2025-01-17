from django.urls import path, include
from rest_framework import routers, permissions
from api.views import ExpenseViewSet, UserRegistrationView, UserLoginView
from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Expense Tracker API",
      default_version='v1',
      description="An API for tracking all your expenses",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="your-email@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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
    path('login/', UserLoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
]