from django.urls import path, include, reverse_lazy
from apps.payments.api.views import PaymentAPIView

urlpatterns = [
   path('', PaymentAPIView.as_view(), name=PaymentAPIView.name),
]
