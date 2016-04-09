#coding=utf-8

from django import forms
from tax.models import Class
from django.core.exceptions import ValidationError

class FeeForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(FeeForm, self).clean()
        return cleaned_data

    def clean_fee(self):
        fee = 0
        fee_str = self.cleaned_data.get("fee")
        if not isinstance(fee,integer):
            try:
                fee = int(fee_str)
            except Exception as e:
                print e
        else:
            fee = fee_str
        return fee

    class Meta:
        model = Class
        fields = ('__all__')