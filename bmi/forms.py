from django import forms
from bmi.models import Userdata

# # class ProductForm(forms.Form):
# #     name = forms.CharField()
# #     price = forms.CharField()
# #     category = forms.CharField()

class BmiCalculateForm(forms.ModelForm):
    class Meta:
        model = Userdata
        fields =("weight", "height")