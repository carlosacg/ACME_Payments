
from django.urls import path
from apps.payments.views import CalculatePaymentRate

app_name = "payments"

urlpatterns = [
    path('', CalculatePaymentRate.as_view(), name=CalculatePaymentRate.name),
]
