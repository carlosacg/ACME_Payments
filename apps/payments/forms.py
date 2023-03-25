from django import forms
from django.utils.translation import ugettext_lazy as _

class EmployeeDataForm(forms.Form):

    input_text = forms.CharField(
        label=_('Input text'),
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': _('Write the data in this field')
        })
    )

    file = forms.FileField(
        required=False
    )
