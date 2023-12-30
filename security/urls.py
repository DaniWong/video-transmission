from django.urls import path, include

app_name = 'security'

urlpatterns = [
    path('api/v1/', include('security.api.urls')),
    # ================================================================================
    # For other non api urls
    # path('customer-create/', views.CustomerCreateView.as_view(), name='customer-create'),
    # ================================================================================
]
