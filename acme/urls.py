
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/',include('apps.payments.urls')),
    path('payments/api',include('apps.payments.api.urls'))
]
