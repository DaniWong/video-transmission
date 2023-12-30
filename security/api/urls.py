from django.urls import path

from .views import CustomTokenObtainPairView, TokenRefreshView


app_name = 'api'


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
