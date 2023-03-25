from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.payments.fnutils import get_amount_to_pay


class PaymentAPIView(APIView):
    name = 'payment_api'

    def post(self, *args, **kwargs):
        try:
            employee_data = self.request.POST.get("employee_data")
            amount_to_pay = get_amount_to_pay(employee_data)
            return Response({"message": amount_to_pay}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error_message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
