from django.urls import path, include

app_name = 'video_transmission'

urlpatterns = [
    path('api/v1/', include('video_transmission.api.urls')),
    # ================================================================================
    # For other non api urls
    # path('customer-create/', views.CustomerCreateView.as_view(), name='customer-create'),
    # ================================================================================
]
