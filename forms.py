from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Product

class ProductForm(ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary w-100'))
    helper.form_action = '/addproduct/'
    helper.form_id = 'p_form'
    class Meta:
        model = Product
        fields = ['name','price', 'quantity','photo']
