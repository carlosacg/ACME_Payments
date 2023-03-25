from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from apps.payments.forms import EmployeeDataForm
from apps.payments.fnutils import process_file


class CalculatePaymentRate(TemplateView):
    name = 'calculate_payment_rate_view'
    template_name = 'payments/calculate_payment.html'

    def get_context_data(self, **kwargs):
        context = super(CalculatePaymentRate, self).get_context_data()
        context.update({
            "form": EmployeeDataForm()
        })
        return context

    def get_success_url(self):
        return reverse_lazy('payments:calculate_payment_rate_view')

    def post(self, *args, **kwargs):
        form = EmployeeDataForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            process_file(self.request.FILES['file'])
        return HttpResponseRedirect(self.get_success_url())
