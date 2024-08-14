from django import forms
from .models import Procurement

class ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = ['branch', 'item', 'quantity', 'cost', 'bill']

    def _init_(self, *args, **kwargs):
        super(ProcurementForm, self)._init_(*args, **kwargs)
        self.fields['branch'].widget.attrs.update({'class': 'form-control'})
        self.fields['item'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Item Name'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Quantity'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Cost'})
        self.fields['bill'].widget.attrs.update({'class': 'form-control'})